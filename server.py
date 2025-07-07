from flask import Flask, request, jsonify
import os
from integrated_pipeline import detect_and_classify_objects
from carbon_helper import format_material_for_frontend, format_subtype_for_frontend

#initialize flask app
app = Flask(__name__)

#set up detect endpoint for accepting post requests
@app.route('/detect', methods=['POST'])
def detect():
    print("📩 Received POST request to /detect")
    if 'image' not in request.files: # request.files contains uploaded files from frontend
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image'] # frontend uploaded file must be named image
    temp_path = f'temp_{image_file.filename}' # original file name
    image_file.save(temp_path) #save file temporarily to run inference

    try:
        print("🧠 Running detection + classification pipeline...")
        # pass to yolo resnet pipeline. 
        detections = detect_and_classify_objects(temp_path, visualize=False)
        print(f"✅ Detections complete: {detections}")
        os.remove(temp_path)
        print("🧹 Temporary image file deleted")
        #in case no objects detected in image 
        if not detections:
            print("⚠️ No detections returned.")
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
        material = top['material_prediction'].lower()
        print(f"🔍 Highest-confidence prediction: {material}")

        # Get only carbon info — this is entire response
        carbon_info = format_material_for_frontend(material)
        print(f"📦 Final carbon info response: {carbon_info}")
        return jsonify(carbon_info)
    # This block catches any errors and deletes the image just in case.
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"🔥 Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

# Separate endpoint for dropdown selection
@app.route('/subtype', methods=['POST'])
def subtype():
    #subtype and material acquired from dict sent by frontend
    print("📩 Received POST request to /subtype")
    data = request.json
    print("📦 Data received:", data)
    material = data.get("material")
    subtype = data.get("subtype")

    if not material or not subtype:
        print("❌ Missing material or subtype")
        return jsonify({"error": "Missing material or subtype"}), 400

    try:
        #get info from helper function for specificity
        carbon_info = format_subtype_for_frontend(material, subtype)
        print("✅ Subtype carbon info:", carbon_info)
        return jsonify(carbon_info)
    except Exception as e:
        print("🔥 Exception in /subtype:", e)
        return jsonify({"error": str(e)}), 400
    
#Starts your Flask server locally on localhost:5001.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

