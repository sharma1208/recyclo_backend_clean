import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
from collections import Counter

# Updated training set transformations:
# - Added RandomGrayscale, GaussianBlur, RandomAdjustSharpness to emphasize texture/reflection differences.
train_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.1),  # slightly stronger jitter
    transforms.RandomGrayscale(p=0.1),       # convert 10% images to grayscale to force texture learning
    transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 2.0)), # blur to simulate reflections/texture variation
    transforms.RandomAdjustSharpness(sharpness_factor=2, p=0.3),  # sharpen to enhance texture edges
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406], 
        std=[0.229, 0.224, 0.225]
    )
])

# Validation set transformations (no augmentation!)
val_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# Load the dataset from folder
dataset = datasets.ImageFolder('datarecyclo/trashnet/data/dataset-resized')

# Calculate class weights for imbalance handling
# Count samples per class (dataset.targets gives labels for ImageFolder)
class_counts = Counter(dataset.targets)
num_samples = sum(class_counts.values())

# Compute weights: inverse of class frequency normalized so sum=number of classes
class_weights = []  # empty list to store weights per class
num_classes = len(dataset.classes) # total number of classes, e.g. 6
for i in range(num_classes): # loop over each class index
    count = class_counts[i] # number of samples in this class i
    weight = num_samples / (num_classes * count)  
    # inverse frequency: total # of all samples in dataset/ (total classes * number of samples in current class)
    class_weights.append(weight) # save the weight for this class
# convert list of floats to a PyTorch tensor, needed for loss function
class_weights = torch.tensor(class_weights, dtype=torch.float)

print("Class counts:", class_counts)
print("Class weights:", class_weights)

# Split dataset into training and validation (80/20 split)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# Apply transformations **after** splitting!
train_dataset.dataset.transform = train_transforms
val_dataset.dataset.transform = val_transforms

# Create DataLoaders for batching
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Check number of classes
num_classes = len(dataset.classes)
print(f"Classes: {dataset.classes}")
print(f"Number of classes: {num_classes}")

# Visualize a few augmented images to confirm transformations
import matplotlib.pyplot as plt

# Get one batch of images and labels from the train_loader iterator
dataiter = iter(train_loader) # Create an iterator from train_loader
images, labels = next(dataiter) # Get the next batch (a set of images and their labels)

# Plot first 4 images in the batch
fig, axs = plt.subplots(1, 4, figsize=(12, 3)) #Set up a figure with 1 row and 4 columns of subplots to display 4 images side by side
for i in range(4):
    img = images[i] # Select the i-th image from the batch (this is a tensor)
    # Un-normalize for better viewing
    img = img * torch.tensor([0.229, 0.224, 0.225]).view(3,1,1) + torch.tensor([0.485, 0.456, 0.406]).view(3,1,1)
    #PyTorch image tensors are in (Channels, Height, Width) format.
    # Matplotlib expects (Height, Width, Channels), so we reorder the axes.
    img = img.permute(1, 2, 0).numpy() # Convert tensor to numpy array for matplotlib
    axs[i].imshow(img)
    axs[i].set_title(f"Label: {labels[i]}")
    axs[i].axis('off')
plt.show()


# Print first batch details
for images, labels in train_loader: # pulls one batch of images and labels
    print("Batch image tensor shape:", images.shape)  # e.g. (batch_size, 3, 224, 224)
    print("Batch labels:", labels)  # tensor of label indices
    break  # just do one batch for now

