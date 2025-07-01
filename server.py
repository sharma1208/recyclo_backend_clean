from flask import Flask, request, jsonify
import os
from integrated_pipeline import detect_and_classify_objects
from carbon_helper import format_material_for_frontend, format_subtype_for_frontend

#initialize flask app
app = Flask(__name__)

#set up detect endpoint for accepting post requests
@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files: # request.files contains uploaded files from frontend
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image'] # frontend uploaded file must be named image
    temp_path = f'temp_{image_file.filename}' # original file name
    image_file.save(temp_path) #save file temporarily to run inference

    try:
        # pass to yolo resnet pipeline. 
        detections = detect_and_classify_objects(temp_path, visualize=False)
        os.remove(temp_path)
        #in case no objects detected in image 
        if not detections:
            return jsonify({
                "material": "unknown",
                "recyclable": False,
                "recycled_carbon_score": None,
                "unrecycled_carbon_score": None,
                "has_subtypes": False,
                "notes": ["No object detected or recognized."]
            })

        # Use the highest-confidence detection and extract its predicted material
        top = detections[0]
        material = top['material'].lower()

        # Get only carbon info — this is entire response
        carbon_info = format_material_for_frontend(material)
        return jsonify(carbon_info)
    # This block catches any errors and deletes the image just in case.
    except Exception as e:
        os.remove(temp_path)
        return jsonify({'error': str(e)}), 500

# Separate endpoint for dropdown selection
@app.route('/subtype', methods=['POST'])
def subtype():
    #subtype and material acquired from dict sent by frontend
    data = request.json
    material = data.get("material")
    subtype = data.get("subtype")

    if not material or not subtype:
        return jsonify({"error": "Missing material or subtype"}), 400

    try:
        #get info from helper function for specificity
        carbon_info = format_subtype_for_frontend(material, subtype)
        return jsonify(carbon_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
#Starts your Flask server locally on localhost:5001.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

