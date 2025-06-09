import torch #main pytorch library
import torch.nn as nn #lets you create or modify neural network layers
from torchvision import models #contains pretrained models like ResNet18
from classification_setup import train_loader, val_loader, num_classes


model = models.resnet18(pretrained=True) #this downloads pretrained weights on ImageNet automatically

# Replacing last layer of ResNet18 for 6 classes instead of 1000
num_classes = 6
model.fc = nn.Linear(model.fc.in_features, num_classes) #model.fc.in_features is the number of inputs to that layer (usually 512 for ResNet18). 
# New linear layer created from 512 -> 6 outputs 

# Moves model to device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

print(model)

criterion = nn.CrossEntropyLoss()  # for classification tasks, loss function to measure model error
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  # common optimizer and learning rate

num_epochs = 14 # Increased to demonstrate early stopping
patience = 3     # How many epochs to wait for improvement before stopping
best_val_accuracy = 0.0 # stores the highest validation accuracy seen so far
epochs_no_improve = 0


for epoch in range(num_epochs):
    model.train()  # Set model to training mode
    
    running_loss = 0.0 # Accumulates total training loss for this epoch

    # TRAINING LOOP - loop over all batches in train_loader
    for batch_idx, (inputs, labels) in enumerate(train_loader):
    # 3. Move inputs and labels to the device (GPU/CPU)
        inputs = inputs.to(device)
        labels = labels.to(device)
    
    # 4. Zero the gradients from previous step
        optimizer.zero_grad()

    # 5. Forward pass: compute predicted outputs by passing inputs to the model
        outputs = model(inputs)
    
    # 6. Calculate the loss aka measures how wrong the model’s predictions are for this batch
        loss = criterion(outputs, labels)
    
    # 7. Backward pass: compute gradient of the loss with respect to model parameters
        loss.backward() # gradients tell how to adjust weights to reduce loss.
    
    # 8. Perform a single optimization step (parameter/weights update)
        optimizer.step() 
    
    # Add batch loss (converted to scalar) to running total   
        running_loss += loss.item()
        
    avg_train_loss = running_loss / len(train_loader)
    print(f"Epoch {epoch+1}/{num_epochs}, Training Loss: {avg_train_loss:.4f}")
    
    # VALIDATION LOOP - evaluate model performance on unseen validation data
    model.eval()  # Set model to evaluation mode (disables dropout, batchnorm updates, etc.)
    val_loss = 0.0  # Accumulate validation loss
    correct = 0     # Count how many predictions are correct
    total = 0       # Count total samples evaluated
    
    with torch.no_grad():  # Disable gradient computation during validation to save memory and computation
        for inputs, labels in val_loader:
            inputs = inputs.to(device)
            labels = labels.to(device)
            
            outputs = model(inputs)  # Forward pass to get predictions
            
            loss = criterion(outputs, labels)  # Compute loss for validation batch
            val_loss += loss.item()  # Accumulate validation loss
            
            # Get predicted classes: torch.max returns (max_value, index_of_max)
            _, predicted = torch.max(outputs, 1)
            
            total += labels.size(0)  # Update total samples count
            
            correct += (predicted == labels).sum().item()  # Add count of correct predictions in batch
            
    avg_val_loss = val_loss / len(val_loader)  # Average validation loss
    val_accuracy = correct / total  # Validation accuracy as a ratio of correct predictions to total samples

    # Print progress for this epoch: training loss, validation loss, and validation accuracy
    print(f"Epoch {epoch+1}/{num_epochs}, "
        f"Train Loss: {avg_train_loss:.4f}, "
        f"Val Loss: {avg_val_loss:.4f}, "
        f"Val Accuracy: {val_accuracy:.4f}")
    
    # Check if validation accuracy improved
    if val_accuracy > best_val_accuracy:
        best_val_accuracy = val_accuracy
        epochs_no_improve = 0  # Reset counter
    
    # Save the best model weights
        torch.save(model.state_dict(), "best_model.pth")
        print(f"Validation accuracy improved. Model saved.")
    else:
        epochs_no_improve += 1
        print(f"No improvement in validation accuracy for {epochs_no_improve} epoch(s).")
        
    # Early stopping condition
    if epochs_no_improve >= patience:
        print(f"Early stopping triggered after {patience} epochs with no improvement.")
        break
    
print("Training complete.")
