import torch
from classification_setup import val_loader, dataset
from train_classifier import model, device
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load best model weights
model.load_state_dict(torch.load("best_model.pth"))
model.eval() #no gradients are tracked

# Store true and predicted labels
y_true = []
y_pred = []

with torch.no_grad(): #Turns off gradient tracking (you’re not training, just evaluating).
    for inputs, labels in val_loader:
        inputs = inputs.to(device)
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1) # Gets the predicted class with the highest probability
        y_true.extend(labels.cpu().numpy())
        y_pred.extend(predicted.cpu().numpy())
    

# Class names
class_names = dataset.classes #So that printed metrics and plots use readable names like "glass" or "plastic" instead of just 0, 1, etc.

# 1️⃣ Classification Report
print("Classification Report:") 
#Prints per-class performance using 
# 1. Precision = TP / (TP + FP) (how often correct) 
# 2. Recall = TP / (TP + FN) (high recall, low misses) 
# 3. F1 = 2 * (Precision * Recall) / (Precision + Recall) (balance between recall and precision)
print(classification_report(y_true, y_pred, target_names=class_names))

# 2️⃣ Confusion Matrix
cm = confusion_matrix(y_true, y_pred)
# Shows actual vs predicted classes:
#Diagonal = correct predictions
#Off-diagonal = mistakes
#Heatmap helps you see patterns of what your model confuses most often

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()

