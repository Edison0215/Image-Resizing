import os
from PIL import Image

def resize_images(directory, width, height):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)
            resized_image = image.resize((width, height))
            resized_image.save(image_path)
            print(f"Resized image: {filename}")

# Specify the directories where the images are located
directories = [r"C:\Users\Acer\Desktop\BC TRAIN"]

# Specify the desired dimensions for the resized images
width = 360
height = 480

# Resize images in each directory
for directory in directories:
    resize_images(directory, width, height)