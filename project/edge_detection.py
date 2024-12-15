import cv2
import numpy as np

def marr_hildreth_edge_detection(image, low_threshold=30, high_threshold=100):
    """
    Detect edges using the Marr-Hildreth edge detector with hysteresis thresholding.

    Parameters:
    - image: Input grayscale image.
    - low_threshold: Lower threshold for hysteresis.
    - high_threshold: Higher threshold for hysteresis.

    Returns:
    - edge_map: Binary edge map of the detected edges.
    """
    # Step 1: Gaussian Smoothing
    smoothed = cv2.GaussianBlur(image, (5, 5), 1.0)

    # Step 2: Compute Laplacian of the smoothed image
    laplacian = cv2.Laplacian(smoothed, cv2.CV_64F)

    # Step 3: Detect zero-crossings
    edge_map = np.zeros_like(image, dtype=np.uint8)
    rows, cols = laplacian.shape

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (laplacian[i, j] > 0 and (laplacian[i - 1, j] < 0 or laplacian[i + 1, j] < 0 or
                                         laplacian[i, j - 1] < 0 or laplacian[i, j + 1] < 0)):
                edge_map[i, j] = 255

    # Step 4: Hysteresis Thresholding
    gradient_magnitude = cv2.Sobel(smoothed, cv2.CV_64F, 1, 0) ** 2 + \
                         cv2.Sobel(smoothed, cv2.CV_64F, 0, 1) ** 2
    gradient_magnitude = np.sqrt(gradient_magnitude)

    final_edge_map = np.zeros_like(edge_map)
    strong_edges = (gradient_magnitude > high_threshold)
    weak_edges = ((gradient_magnitude >= low_threshold) & (gradient_magnitude <= high_threshold))

    final_edge_map[strong_edges] = 255

    def propagate_edges(i, j):
        if weak_edges[i, j] and final_edge_map[i, j] == 0:
            final_edge_map[i, j] = 255
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0 <= i + di < rows and 0 <= j + dj < cols:
                        propagate_edges(i + di, j + dj)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if strong_edges[i, j]:
                propagate_edges(i, j)

    return final_edge_map

if __name__ == '__main__':
    # Example usage
    input_image = cv2.imread('example.jpg', cv2.IMREAD_GRAYSCALE)

    if input_image is None:
        print("Error: Image not found. Please check the file path.")
        exit(1)

    edges = marr_hildreth_edge_detection(input_image)

    # Display the result
    cv2.imshow('Detected Edges', edges)

    # Save the output image
    output_filename = 'detected_edges.png'
    cv2.imwrite(output_filename, edges)
    print(f"Output image saved as: {output_filename}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
