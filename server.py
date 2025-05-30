from flask import Flask, request, jsonify
import os
from recycle_det import detect_and_classify

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    temp_path = f'temp_{image_file.filename}'
    image_file.save(temp_path)

    try:
        detections = detect_and_classify(temp_path, visualize=False)
        if not detections:
            return jsonify({
                'class_name': 'Unknown',
                'recyclable': False,
                'carbonScore': 'Unknown',
                'material': 'Unknown'
            })

        # Just use the top prediction for now (enhance this later)
        top = detections[0]
        class_name = top['class_name']
        material = top['material'].lower()

        # Example simple logic for recyclable and carbonScore:
        recyclable_materials = ['plastic', 'glass', 'metal', 'paper', 'cardboard']
        recyclable = material in recyclable_materials

        # Simple carbon score logic (customize as you want)
        if material in ['plastic', 'metal']:
            carbon_score = 'High'
        elif material in ['paper', 'cardboard']:
            carbon_score = 'Low'
        else:
            carbon_score = 'Medium'

        response = {
            'class_name': class_name,
            'recyclable': recyclable,
            'carbonScore': carbon_score,
            'material': material.capitalize()
        }

    except Exception as e:
        os.remove(temp_path)
        return jsonify({'error': str(e)}), 500

    os.remove(temp_path)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

