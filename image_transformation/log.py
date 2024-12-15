import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image5.jpg', 0)

# 2. Log Transformation
def log_transformation(image):
    c = 200 / np.log(1 + np.max(image))
    log_transformed = c * np.log(1 + image)
    return np.array(log_transformed, dtype=np.uint8)

img_log = log_transformation(img)


# Displaying the images
plt.figure(figsize=(20, 20))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Log Transformation
plt.subplot(1, 2, 2)
plt.imshow(img_log, cmap='gray')
plt.title('Log Transformation')
plt.axis('off')


plt.show()
