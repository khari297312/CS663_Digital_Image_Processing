# plot the histogram of image
# import all the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale mode
img = cv2.imread('Picture3.png', 0)
 
# Check if the image is loaded successfully
if img is None:
   raise FileNotFoundError("Image could not be loaded. Check the file path.")

# Display the histogram of the image
plt.hist(img.ravel(), 256, [0, 256], color='r', alpha=0.5, label='Image 1')
plt.legend(loc='upper right')

# Save the histogram as an image
plt.savefig('histogram.png') 