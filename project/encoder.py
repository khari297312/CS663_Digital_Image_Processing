import cv2
import numpy as np

def encoder(image_path, mask_path, masked_image_path):
    """
    Encoder function that generates an edge-based mask and saves the mask and masked image.
    
    Parameters:
    - image_path: Path to the input image (3-channel RGB image).
    - mask_path: Path to save the generated mask (e.g., .png format).
    - masked_image_path: Path to save the masked image (e.g., .png format).
    """
    # Step 1: Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found. Please check the file path.")
        return

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Step 2: Edge Detection using Canny
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)

    # Step 3: Initialize the mask (all ones)
    mask = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Step 4: Exclude the neighborhood of edge pixels
    window = 3  # Size of the neighborhood
    pd = (window - 1) // 2

    # Pad the mask to handle edge pixels without index errors
    padded_mask = np.pad(mask, ((pd, pd), (pd, pd), (0, 0)), mode='constant', constant_values=255)

    # Iterate through the padded mask and update the neighborhood of edge pixels
    for i in range(pd, pd + height):
        for j in range(pd, pd + width):
            if edges[i - pd, j - pd] > 0:
                padded_mask[i - pd:i + pd + 1, j - pd:j + pd + 1, :] = 0

    # Extract the mask back to the original size
    mask = padded_mask[pd:pd + height, pd:pd + width, :]

    # Step 5: Exclude boundary pixels of the image in the mask
    mask[0, :, :] = 0
    mask[height - 1, :, :] = 0
    mask[:, 0, :] = 0
    mask[:, width - 1, :] = 0

    # Step 6: Create the masked image by applying the inverted mask
    masked_image = cv2.bitwise_and(image, mask)

    # Display the mask and masked image
    cv2.imshow("Mask", mask)
    cv2.imshow("Masked Image", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Step 7: Save the mask and masked image
    # Convert the mask to binary (logical) before saving
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    mask = (mask > 0).astype(np.uint8) * 255  # Convert to binary mask (0 or 255)

    cv2.imwrite(mask_path, mask)
    cv2.imwrite(masked_image_path, masked_image)
    print(f"Mask saved as: {mask_path}")
    print(f"Masked image saved as: {masked_image_path}")

if __name__ == '__main__':
    # Example usage
    encoder('data/im1.png', 'data/mask.png', 'data/masked_image.png')
