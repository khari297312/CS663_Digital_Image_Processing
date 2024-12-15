import cv2
import numpy as np
import zlib
import pickle

def edge_detection(image):
    """
    Detect edges using the Marr-Hildreth (Laplacian of Gaussian) method.
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Laplacian of Gaussian
    edges = cv2.Laplacian(blurred, cv2.CV_64F)
    edges = np.uint8(np.absolute(edges))

    # Apply hysteresis thresholding (Canny-style)
    edge_map = cv2.Canny(edges, 50, 150)
    
    return edge_map

def extract_pixel_values(image, edge_map, q=4, d=5):
    """
    Extract pixel values on both sides of the detected edges.
    Quantize and subsample the values.
    """
    # Get image dimensions
    height, width = image.shape[:2]

    # Initialize list to store pixel values
    pixel_values = []

    # Iterate through edge map and extract pixel values
    for y in range(0, height, d):
        for x in range(0, width, d):
            if edge_map[y, x] > 0:
                # Take pixel values from both sides of the edge
                left_val = image[y, max(x-1, 0)]
                right_val = image[y, min(x+1, width-1)]
                pixel_values.append((left_val, right_val))

    # Quantize the pixel values to 2^q levels
    pixel_values = np.array(pixel_values) // (256 // (2 ** q))
    return pixel_values

def compress_data(edge_map, pixel_values):
    """
    Compress edge map and pixel values using PNG and zlib respectively.
    """
    # Compress edge map using PNG format (lossless)
    _, edge_map_compressed = cv2.imencode('.png', edge_map)

    # Compress pixel values using zlib
    pixel_values_compressed = zlib.compress(pickle.dumps(pixel_values))

    return edge_map_compressed, pixel_values_compressed

def save_encoded_data(filename, q, d, edge_map_compressed, pixel_values_compressed):
    """
    Save encoded data to a file.
    """
    with open(filename, 'wb') as f:
        # Store quantization parameter and sampling distance
        header = {'q': q, 'd': d}
        pickle.dump((header, edge_map_compressed, pixel_values_compressed), f)

def encode_image(image, q=4, d=5, output_filename='compressed_image.dat'):
    """
    Full encoding process of the image.
    """
    # Step 1: Edge Detection
    edge_map = edge_detection(image)

    # Step 2: Extract Pixel Values
    pixel_values = extract_pixel_values(image, edge_map, q, d)

    # Step 3: Compress Data
    edge_map_compressed, pixel_values_compressed = compress_data(edge_map, pixel_values)

    # Step 4: Save Encoded Data
    save_encoded_data(output_filename, q, d, edge_map_compressed, pixel_values_compressed)
    print("Encoding complete. Data saved to:", output_filename)

def load_encoded_data(filename):
    """
    Load encoded data from a file.
    """
    with open(filename, 'rb') as f:
        header, edge_map_compressed, pixel_values_compressed = pickle.load(f)
    return header, edge_map_compressed, pixel_values_compressed

def decompress_data(edge_map_compressed, pixel_values_compressed):
    """
    Decompress edge map and pixel values.
    """
    # Decompress edge map
    edge_map = cv2.imdecode(np.frombuffer(edge_map_compressed, np.uint8), cv2.IMREAD_GRAYSCALE)

    # Decompress pixel values
    pixel_values = pickle.loads(zlib.decompress(pixel_values_compressed))

    return edge_map, pixel_values

def homogeneous_diffusion(image, edge_map):
    """
    Inpaint missing pixel values using homogeneous diffusion (Laplace equation).
    """
    # Create mask where edge pixels are 0 (known) and others are 1 (unknown)
    mask = (edge_map == 0).astype(np.uint8)

    # Inpainting using OpenCV's inpaint method with homogeneous diffusion
    inpainted_image = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
    
    return inpainted_image

def decode_image(input_filename):
    """
    Full decoding process of the image.
    """
    # Step 1: Load Encoded Data
    header, edge_map_compressed, pixel_values_compressed = load_encoded_data(input_filename)
    q, d = header['q'], header['d']

    # Step 2: Decompress Data
    edge_map, pixel_values = decompress_data(edge_map_compressed, pixel_values_compressed)

    # Step 3: Reconstruct Image using Inpainting
    reconstructed_image = homogeneous_diffusion(edge_map, edge_map)

    return reconstructed_image

if __name__ == '__main__':
    # Example usage
    input_image = cv2.imread('example.jpg')
    output_filename = 'compressed_image.dat'

    # Encoding
    encode_image(input_image, q=4, d=5, output_filename=output_filename)

    # Decoding
    decoded_image = decode_image(output_filename)
    cv2.imshow('Decoded Image', decoded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
