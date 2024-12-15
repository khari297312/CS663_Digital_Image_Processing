import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load images in grayscale mode
img1 = cv2.imread('Picture1.jpg', 0)
img2 = cv2.imread('Picture2.jpg', 0)

# Check if images are loaded successfully
if img1 is None:
    raise FileNotFoundError("Image1 could not be loaded. Check the file path.")
if img2 is None:
    raise FileNotFoundError("Image2 could not be loaded. Check the file path.")

# Ensure images have the same dimensions
if img1.shape != img2.shape:
    raise ValueError("Both images must have the same dimensions.")

# Initialize joint histogram
joint_hist = np.zeros((256, 256))

# Populate the joint histogram
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        joint_hist[img1[i, j], img2[i, j]] += 1

# Display the joint histogram
#show in blue scale
plt.imshow(joint_hist)
plt.title('Joint Histogram')
plt.xlabel('Pixel Intensities of Image 1')
plt.ylabel('Pixel Intensities of Image 2')
plt.colorbar()
plt.show()

# Save the joint histogram as an image
# Normalize joint histogram for better visualization
joint_hist_normalized = cv2.normalize(joint_hist, None, 0, 255, cv2.NORM_MINMAX)
# cv2.imwrite('joint_hist.png', joint_hist_normalized)

# Save the joint histogram as a text file
# np.savetxt('joint_hist.txt', joint_hist)

# Save the joint histogram as a CSV file
# np.savetxt('joint_hist.csv', joint_hist, delimiter=',')


#plot only for intensity from 0 to 60
