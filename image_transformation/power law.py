import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image3.jpg', 0)

# Power-Law (Gamma) Transformation
def power_law_transformation(image, gamma=1.0):
    if gamma == 0:
        gamma = 0.1  # Avoid gamma = 0 to prevent division by zero issues
    c = 255 / (np.max(image) ** gamma)
    gamma_transformed = c * (image ** gamma)
    return np.array(gamma_transformed, dtype=np.uint8)

# Displaying the images
plt.figure(figsize=(20, 20))

# Generate and plot 12 images with different gamma values
for i in range(1, 13):  # Start from 1 to avoid gamma=0
    gamma_value = i * 0.2  # Adjust the gamma value for each image
    img_gamma = power_law_transformation(img, gamma=gamma_value)
    
    plt.subplot(3, 4, i)
    plt.imshow(img_gamma, cmap='gray')
    plt.title(f'Gamma={gamma_value:.1f}')
    plt.axis('off')

plt.show()
