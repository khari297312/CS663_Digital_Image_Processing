import cv2
import numpy as np

def save_edge_map(edge_map, output_filename='edge_map.png'):
    """
    Save the bi-level edge map using lossless PNG compression.

    Parameters:
    - edge_map: The binary edge map obtained from edge detection.
    - output_filename: The filename for the saved edge map.
    """
    # Ensure the edge map is binary (0 and 255 values)
    binary_edge_map = np.where(edge_map > 0, 255, 0).astype(np.uint8)

    # Save the edge map using PNG format for lossless compression
    cv2.imwrite(output_filename, binary_edge_map)
    print(f"Edge map saved as: {output_filename}")

if __name__ == '__main__':
    # Example usage
    input_image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)

    if input_image is None:
        print("Error: Image not found. Please check the file path.")
        exit(1)

    # Step 1: Detect edges using Marr-Hildreth edge detector
    def marr_hildreth_edge_detection(image):
        smoothed = cv2.GaussianBlur(image, (5, 5), 1.0)
        laplacian = cv2.Laplacian(smoothed, cv2.CV_64F)
        edge_map = np.zeros_like(image, dtype=np.uint8)
        rows, cols = laplacian.shape

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if (laplacian[i, j] > 0 and (laplacian[i - 1, j] < 0 or laplacian[i + 1, j] < 0 or
                                             laplacian[i, j - 1] < 0 or laplacian[i, j + 1] < 0)):
                    edge_map[i, j] = 255

        return edge_map

    # Perform edge detection
    edges = marr_hildreth_edge_detection(input_image)

    # Step 2: Encode and save the contour location
    save_edge_map(edges, 'encoded_edge_map.png')
