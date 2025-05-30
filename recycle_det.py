from ultralytics import YOLO 
import cv2
import matplotlib.pyplot as plt

def detect_and_classify(image_path, visualize=False, output_path=None):
    model = YOLO('yolov8n.pt')
    results = model.predict(image_path)
    all_detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])  # class id
            conf = box.conf[0].item()  # confidence score
            coords = box.xyxy[0].tolist()  # box coordinates as list [x1,y1,x2,y2]
            class_name = result.names[cls_id]
            corrected_class = correct_misclassifications(class_name, conf, coords)
            material = classify_material(corrected_class)
            print(f'Detected {corrected_class} ({material}) with confidence {conf:.2f} at {coords}')
            all_detections.append({
                'class_name': corrected_class,
                'material': material,
                'conf': round(conf, 2),
                'coords':  [round(c, 2) for c in coords]
            })
    if visualize:
        if not output_path:
            output_path = image_path.replace('.jpg', '_detected.jpg')
        draw_det(image_path, all_detections)  # Only show plot if requested
        
    return all_detections


def classify_material(class_name):
    plastic_items = ['bottle', 'cup', 'jug']
    aluminum_items = ['can']
    paper_items = ['book', 'magazine', 'newspaper']
    glass_items = ['wine glass', 'vase']
    cardboard_items = ['box', 'carton']
    
    if class_name in plastic_items:
        return 'Plastic'
    elif class_name in aluminum_items:
        return 'Aluminum'
    elif class_name in paper_items:
        return 'Paper'
    elif class_name in glass_items:
        return 'Glass'
    elif class_name in cardboard_items:
        return 'Cardboard'
    else:
        return 'Unknown'
    
def correct_misclassifications(class_name, conf, box_coords):
    """
    Override obvious misclassifications based on context.
    """
    # If YOLO thinks multiple "vases" are present and confidence is high,
    # it's likely plastic bottles in a recycling context
    if class_name == 'vase' and conf > 0.5:
        return 'bottle'
    
    # Add more rules here later
    return class_name  

def draw_det(image_path, detections, output_path=None):
    img = cv2.imread(image_path)
    for det in detections:
        coords = list(map(int, det['coords']))
        label = f"{det['class_name']} ({det['material']}) {det['conf']:.2f}"
        color = (255, 0, 0)  # Green box
        cv2.rectangle(img, (coords[0], coords[1]), (coords[2], coords[3]), color, 2)
        cv2.putText(img, label, (coords[0], coords[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        # Convert BGR to RGB for matplotlib
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img_rgb)
    #plt.axis('off')
    #plt.title("Detections")
    # plt.show()
    if output_path:
        cv2.imwrite(output_path, img)
            
# This lets you run the function when you launch the script directly
if __name__ == '__main__':
    # Replace 'zidane.jpg' with your test image
    detections = detect_and_classify('plastic-bottles.jpg', visualize=False)
    print(detections)