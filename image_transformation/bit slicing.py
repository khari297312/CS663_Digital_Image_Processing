import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
img = cv2.imread('image1.jpg', 0)

#bit slicing
#One can compress an image (with some loss!) by using the most significant bits from Q’ to Q, as follows:

def bit_slicing(image, Q, Q_):
    return np.bitwise_and(image, 2**Q +2**Q_)
# Displaying the images
plt.figure(figsize=(20, 20))
count=1
for i in range(1, 9):
    for j in range(1, 9):
        bit = bit_slicing(img, i, (i+j)%8+1)
        plt.subplot(8, 8, count)
        plt.imshow(bit, cmap='gray')
        plt.title(str(i)+' and ' + str((i+j)%8+1))
        plt.axis('off')
        count += 1

plt.show()