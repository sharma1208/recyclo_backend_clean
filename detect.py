from PIL import Image

try:
    img = Image.open("bus.jpg")
    img.show()
    print("Image loaded successfully!")
except Exception as e:
    print("Error loading image:", e)
