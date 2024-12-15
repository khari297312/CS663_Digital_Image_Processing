import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image1.jpg', 0)

#bit plane slicing
def bit_plane_slicing(image, bit):
    return np.bitwise_and(image, 2**bit)

# Displaying the images
plt.figure(figsize=(20, 20))

for i in range(1, 9):
    bit = bit_plane_slicing(img, i-1)
    plt.subplot(4, 2, i)
    plt.imshow(bit, cmap='gray')
    plt.title('Bit Plane ' + str(i))
    plt.axis('off')

plt.show()
