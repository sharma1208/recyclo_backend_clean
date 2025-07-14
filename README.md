# 🧠 RecycloVision Backend (Flask + PyTorch)

The backend of **RecycloVision**, an AI-powered recycling assistant that detects waste materials in images and returns real-world carbon impact insights. Built with Flask and PyTorch, it uses a YOLOv8 object detector and a fine-tuned ResNet classifier to analyze user-uploaded images and provide accurate recycling information.

---

## 🧱 Tech Stack

- **Framework**: Flask (Python)
- **Object Detection**: YOLOv8 (Ultralytics)
- **Classification**: ResNet18 (PyTorch + torchvision)
- **Data Augmentation**: `torchvision.transforms`
- **Dataset**: Modified TrashNet
- **Carbon Data Source**:  
  📄 All carbon impact values and notes are derived from [this research doc](https://docs.google.com/document/d/1mpNn4O6omvFz1nVS7oDDm8AUep3Bp1QR3uyGqwosTNE/edit?usp=sharing)

## 📦 Folder Structure

backend/
├── classification_setup.py # Data loaders, transforms, and class weights
├── train_classifier.py # ResNet fine-tuning with early stopping
├── integrated_pipeline.py # Runs YOLO detection + ResNet classification
├── server.py # Flask app with /detect, /subtype, /report_misclassification endpoints
├── carbon_helper.py # Carbon data formatting for frontend
├── carbon_data.py # Core data on materials & subtypes
├── retrain_from_misclass.py # Pulls misclassified images and retrains model
├── logs/ # Folder for storing JSON misclassification reports
└── best_model.pth # Saved PyTorch weights from latest best model

````

---

## 🧪 Endpoints

### 🔍 `POST /detect`

Uploads an image, runs it through YOLO + ResNet, and returns predicted material + carbon data.

```json
{
  "material": "plastic",
  "recyclable": true,
  "recycled_carbon_score": 1.2,
  "unrecycled_carbon_score": 4.8,
  "notes": ["Commonly recyclable", "High energy cost when landfilled"],
  ...
}
````

### 🔁 `POST /subtype`

If a user selects a specific subtype (e.g., LDPE plastic), return updated carbon impact.

**Request:**

```json
{
  "material": "plastic",
  "subtype": "LDPE"
}
```

**Response:** same structure as `/detect`, with subtype-specific data.

### 🐛 `POST /report_misclassification`

Logs incorrect predictions reported by users (includes original label, corrected label, timestamp, and image path).

```json
{
  "original": {
    "material": "glass",
    "image_path": "path/to/image.jpg"
  },
  "corrected_material": "plastic",
  "timestamp": "2025-07-14T12:30:00Z"
}
```

---

## �� Model Training

Train the ResNet classifier with:

```bash
python train_classifier.py
```

- Uses **transfer learning** from ImageNet
- Freezes all but last two ResNet layers
- Applies strong texture-based augmentations:

  - `GaussianBlur`, `RandomGrayscale`, `ColorJitter`, etc.

- Uses **class weights** to handle dataset imbalance
- Supports **early stopping** based on validation accuracy

---

## 🔁 Retraining from User Reports

To include misclassification corrections into your training set:

```bash
python retrain_from_misclass.py
```

- Copies user-corrected images to correct class folder
- Automatically triggers a new training session
- Appends to your dataset and updates `best_model.pth`

---

## 📤 Deployment Notes

- Run the server locally:

```bash
python server.py
```

- Consider Dockerizing the app for production
- When deploying on mobile or web, replace `localhost` with the server's actual IP or domain

---

## 📊 Carbon Impact Data

All carbon impact scores, recycling notes, and material subtype data are based on extensive research found in this shared document:

🔗 [RecycloVision Carbon Research Source](https://docs.google.com/document/d/1mpNn4O6omvFz1nVS7oDDm8AUep3Bp1QR3uyGqwosTNE/edit?usp=sharing)

---

## 🚀 Future Work

- [ ] Extend detection to support **batch image uploads**
- [x] Add **mini-game rewards** for recycling progress
- [ ] Add frontend UI for **reporting and subtype selection**
- [ ] Improve model with **dynamic augmentation** pipelines
- [ ] Deploy API with **Docker** and host on **cloud**
- [ ] Expand dataset with **more diverse samples and classes**

---

## 💚 Built for Sustainability

Help users make better recycling decisions — powered by AI and backed by real carbon data.
