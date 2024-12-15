#writing code for image transformation :
#1: negative transformation

# import all the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale mode
img = cv2.imread('image1.jpg', 0)

# Check if the image is loaded successfully
if img is None:
    raise FileNotFoundError("Image could not be loaded. Check the file path.")

# Negative transformation
def negative_transformation(img):
    img_negative = 255 - img
    return img_negative

# Apply the transformations
img_negative = negative_transformation(img)

plt.figure(figsize=(20, 20))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img_negative, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

plt.show()
# Save the images

