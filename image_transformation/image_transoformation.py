#writing code for image transformation :
#1: negative transformation
#2: log transformation
#3: power-law transformation
#4: contrast stretching transformation
#5: histogram equalization transformation
#6: histogram specification transformation

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

# Log transformation
def log_transformation(img):
    c = 255 / np.log(1 + np.max(img))
    img_log = c * np.log(1 + img)
    return img_log

# Power-law transformation
def power_law_transformation(img, gamma):
    img_power_law = np.power(img, gamma)
    return img_power_law

# Contrast stretching transformation
def contrast_stretching_transformation(img, r1, s1, r2, s2):
    img_contrast_stretching = np.piecewise(img, [img < r1, (img >= r1) & (img <= r2), img > r2], [lambda img: s1 / r1 * img, lambda img: ((s2 - s1) / (r2 - r1)) * (img - r1) + s1, lambda img: ((255 - s2) / (255 - r2)) * (img - r2) + s2])
    return img_contrast_stretching

# Histogram equalization transformation
def histogram_equalization_transformation(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    img_histogram_equalization = np.interp(img.flatten(), bins[:-1], cdf_normalized)
    return img_histogram_equalization.reshape(img.shape)

# Histogram specification transformation
def histogram_specification_transformation(img, img_ref):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    hist_ref, bins_ref = np.histogram(img_ref.flatten(), 256, [0, 256])
    cdf_ref = hist_ref.cumsum()
    cdf_normalized_ref = cdf_ref * hist_ref.max() / cdf_ref.max()
    
    img_histogram_specification = np.interp(cdf_normalized, cdf_normalized_ref, bins_ref[:-1])
    return img_histogram_specification.reshape(img.shape)

# Apply the transformations
img_negative = negative_transformation(img)
# img_log = log_transformation(img)
# img_power_law = power_law_transformation(img, 0.5)
# img_contrast_stretching = contrast_stretching_transformation(img, 50, 0, 200, 255)
# img_histogram_equalization = histogram_equalization_transformation(img)
# img_histogram_specification = histogram_specification_transformation(img, img)
# Display the images
plt.figure(figsize=(20, 20))
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img_negative, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

# plt.subplot(2, 3, 3)
# plt.imshow(img_log, cmap='gray')
# plt.title('Log Transformation')
# plt.axis('off')

# plt.subplot(2, 3, 4)
# plt.imshow(img_power_law, cmap='gray')
# plt.title('Power-law Transformation')

# plt.subplot(2, 3, 5)
# plt.imshow(img_contrast_stretching, cmap='gray')
# plt.title('Contrast Stretching Transformation')

# plt.subplot(2, 3, 6)
# plt.imshow(img_histogram_equalization, cmap='gray')
# plt.title('Histogram Equalization Transformation')

plt.show()
# Save the images

