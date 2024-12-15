import cv2
import numpy as np

def decoder(mask_path, masked_image_path, save_path):
    """
    Decoder function using homogeneous diffusion for image reconstruction.
    
    Parameters:
    - mask_path: Path to the mask image (binary mask).
    - masked_image_path: Path to the masked image with missing pixels.
    - save_path: Path to save the reconstructed image.
    """
    # Step 1: Read the masked image and mask
    masked_image = cv2.imread(masked_image_path).astype(np.float64)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE).astype(np.float64)
    
    if masked_image is None or mask is None:
        print("Error: Image or mask not found. Please check the file paths.")
        return

    # Step 2: Prepare the mask for 3 channels (RGB)
    mask = mask / 255.0  # Normalize mask to [0, 1]
    mask = np.stack([mask] * 3, axis=-1)  # Expand mask to 3 channels (RGB)

    # Step 3: Diffusion parameters
    delta_t = 0.1  # Time step size
    max_iterations = 500  # Number of iterations

    # Step 4: Pad the masked image to handle boundary conditions
    padded_image = np.pad(masked_image, ((1, 1), (1, 1), (0, 0)), mode='edge')
    height, width, _ = masked_image.shape

    # Step 5: Homogeneous Diffusion Process
    for _ in range(max_iterations):
        # Compute the Laplacian (second derivatives)
        res_xx = padded_image[1:height+1, 2:width+2, :] - 2 * padded_image[1:height+1, 1:width+1, :] + padded_image[1:height+1, 0:width, :]
        res_yy = padded_image[2:height+2, 1:width+1, :] - 2 * padded_image[1:height+1, 1:width+1, :] + padded_image[0:height, 1:width+1, :]
        Laplacian = res_xx + res_yy

        # Update the masked image using the Laplacian and mask
        padded_image[1:height+1, 1:width+1, :] += delta_t * Laplacian * mask

    # Step 6: Extract the reconstructed image from the padded array
    reconstructed_image = padded_image[1:height+1, 1:width+1, :]

    # Step 7: Convert the image back to uint8 format
    reconstructed_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)

    # Step 8: Save and display the reconstructed image
    cv2.imwrite(save_path, reconstructed_image)
    print(f"Reconstructed image saved as: {save_path}")

    cv2.imshow("Reconstructed Image", reconstructed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Example usage
    decoder('data/mask.png', 'data/masked_image.png', 'data/restored_image.png')
