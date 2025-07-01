import torch # for tensor operations & deep learning 
import torch.nn as nn # loads neural network components
from torchvision import models # access to resnet18 prebuilt model 
from ultralytics import YOLO #loads YOLOv8 model
import cv2 #for image manipulation (drawing, loading)
from PIL import Image #cropping and transforming images
from classification_setup import val_transforms, dataset # euses your validation transforms (resize, normalize) and dataset.classes for label names.

# --- Load YOLOv8 Model for Object Detection ---
yolo_model = YOLO("yolov8n.pt")

# --- Load Fine-Tuned ResNet Classifier ---
classifier = models.resnet18() #loads base resnet18
classifier.fc = nn.Linear(512, len(dataset.classes))  #Replaces its final layer (fc) with a new Linear layer that has len(dataset.classes) outputs.
#512 -> 6
classifier.load_state_dict(torch.load("best_model.pth")) # loads fine tuned weights
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") #move model to gpu or cpu
classifier.to(device)
classifier.eval() # eval mode to disable batch norm updates and dropout

# --- Detection + Classification Pipeline ---
def detect_and_classify_objects(image_path, visualize=False, output_path=None): #will not draw boxes and save images automatically visualize=False
    # Load image using OpenCV
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #loads BGR image convert to RGB for PyTorch
    
    results = yolo_model.predict(image_path)[0] #runs yolov8 on image and gets detection result
    #for first image
    detections = []

    #loop over detections
    for box in results.boxes:
        cls_id = int(box.cls[0]) #yolo predicted class
        conf = float(box.conf[0]) #yolo confidence score
        x1, y1, x2, y2 = map(int, box.xyxy[0]) #coords of bounding box
        
        # Crop the detected region
        crop = image_rgb[y1:y2, x1:x2] #crop just detected object
        pil_crop = Image.fromarray(crop) #convert to PIL so we can use val_transforms

        # Preprocess using same validation transforms, apply resize and normalize transforms
        # from training and add batch dimension to get [1,3,224,224] shape, send to same device as 
        # our model. 
        input_tensor = val_transforms(pil_crop).unsqueeze(0).to(device)

        # Run through classifier
        with torch.no_grad(): #disable gradient 
            output = classifier(input_tensor) #raw output from model
            pred_idx = torch.argmax(output, dim=1).item() #find index of highest logit to get predicted class
            material = dataset.classes[pred_idx] #material from classifier

        # Add detection info
        detections.append({
            'original_class': results.names[cls_id],
            'material_prediction': material,
            'confidence': round(conf, 2),
            'coords': [x1, y1, x2, y2]
        })

        print(f"Detected {results.names[cls_id]} as {material} with conf {conf:.2f} at {x1, y1, x2, y2}")

        # Optional draw of bounding boxes
        if visualize:
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{material} ({conf:.2f})"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    #save annotated image 
    if visualize:
        output_path = output_path or image_path.replace(".jpg", "_classified.jpg")
        cv2.imwrite(output_path, image)
    #return detection results
    return detections

# --- Run directly ---
if __name__ == '__main__':
    path = "example.jpg"  # replace with your test image
    results = detect_and_classify_objects(path, visualize=True)
    print(results)
