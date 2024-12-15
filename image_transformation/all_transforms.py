import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image1.jpg', 0)

# 1. Negative Transformation
def negative_transformation(image):
    return 255 - image

img_negative = negative_transformation(img)

# 2. Log Transformation
def log_transformation(image):
    c = 255 / np.log(1 + np.max(image))
    log_transformed = c * np.log(1 + image)
    return np.array(log_transformed, dtype=np.uint8)

img_log = log_transformation(img)

# 3. Power-Law (Gamma) Transformation
def power_law_transformation(image, gamma=1.0):
    c = 255 / np.max(image) ** gamma
    gamma_transformed = c * (image ** gamma)
    return np.array(gamma_transformed, dtype=np.uint8)

img_gamma = power_law_transformation(img, gamma=2.0)

# 4. Contrast Stretching Transformation
def contrast_stretching(image):
    p_min = np.min(image)
    p_max = np.max(image)
    contrast_stretched = (image - p_min) * 255 / (p_max - p_min)
    return np.array(contrast_stretched, dtype=np.uint8)

img_contrast = contrast_stretching(img)

# 5. Histogram Equalization
def histogram_equalization(image):
    return cv2.equalizeHist(image)

img_hist_eq = histogram_equalization(img)

# 6. Histogram Specification (Matching)
def histogram_specification(source, template):
    source_hist, bins = np.histogram(source.flatten(), 256, [0, 256])
    template_hist, bins = np.histogram(template.flatten(), 256, [0, 256])

    source_cdf = source_hist.cumsum()
    source_cdf = (source_cdf / source_cdf[-1]) * 255

    template_cdf = template_hist.cumsum()
    template_cdf = (template_cdf / template_cdf[-1]) * 255

    lookup_table = np.zeros(256)
    for i in range(256):
        closest_value = np.argmin(np.abs(template_cdf - source_cdf[i]))
        lookup_table[i] = closest_value

    specified_img = cv2.LUT(source, lookup_table.astype('uint8'))
    return specified_img

# For demonstration, use the original image as the template
img_specified = histogram_specification(img, img)

# Displaying the images
plt.figure(figsize=(20, 20))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Negative Transformation
plt.subplot(2, 3, 2)
plt.imshow(img_negative, cmap='gray')
plt.title('Negative Transformation')
plt.axis('off')

# Log Transformation
plt.subplot(2, 3, 3)
plt.imshow(img_log, cmap='gray')
plt.title('Log Transformation')
plt.axis('off')

# Power-Law (Gamma) Transformation
plt.subplot(2, 3, 4)
plt.imshow(img_gamma, cmap='gray')
plt.title('Gamma Transformation')
plt.axis('off')

# Contrast Stretching
plt.subplot(2, 3, 5)
plt.imshow(img_contrast, cmap='gray')
plt.title('Contrast Stretching')
plt.axis('off')

# Histogram Equalization
plt.subplot(2, 3, 6)
plt.imshow(img_hist_eq, cmap='gray')
plt.title('Histogram Equalization')
plt.axis('off')

# Uncomment and run the following block if you also want to display histogram specification
# # Histogram Specification (this uses the original image as a template for simplicity)
# plt.subplot(2, 3, 7)
# plt.imshow(img_specified, cmap='gray')
# plt.title('Histogram Specification')
# plt.axis('off')

plt.show()
