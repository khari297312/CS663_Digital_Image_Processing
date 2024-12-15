import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image5.jpg', 0)

# Contrast Stretching Transformation
def contrast_stretching(image):
    p_min = np.min(image)
    p_max = np.max(image)
    
    # Check if p_min and p_max are the same
    if p_min == p_max:
        return np.zeros(image.shape, dtype=np.uint8)
    
    # Apply contrast stretching transformation
    contrast_stretched = (image - p_min) * 255.0 / (p_max - p_min)
    
    # Clip the values to the 0-255 range and convert to uint8
    contrast_stretched = np.clip(contrast_stretched, 0, 255)
    
    return np.array(contrast_stretched, dtype=np.uint8)

img_contrast = contrast_stretching(img)

# Displaying the images
plt.figure(figsize=(15, 15))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Contrast Stretching
plt.subplot(1, 2, 2)
plt.imshow(img_contrast, cmap='gray')
plt.title('Contrast Stretching')
plt.axis('off')

plt.show()
