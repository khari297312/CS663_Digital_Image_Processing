% Load images
im1 = imread('goi1.jpg');
im2 = imread('goi2.jpg');

% Convert images to double precision
im1 = double(im1);
im2 = double(im2);

% Assume affine_matrix is the affine transformation matrix obtained from control points
% Replace with your actual matrix
% affine_matrix = [Your generated matrix here];

% Invert the affine transformation matrix for backward warping
inv_matrix = inv(problem6_a_matrix);

% Get the dimensions of the second image (output image)
[rows, cols, channels] = size(im2);

% Initialize the output (warped) image
warped_image = zeros(rows, cols, channels);

% Perform nearest-neighbor interpolation
for i = 1:rows
    for j = 1:cols
        % Apply the inverse affine transformation to map output (warped) coordinates to input (im1) coordinates
        original_coords = inv_matrix * [j; i; 1];
        
        % Extract the original x and y coordinates
        x_orig = round(original_coords(1));
        y_orig = round(original_coords(2));
        
        % Check if the original coordinates are within the bounds of the first image
        if x_orig >= 1 && x_orig <= size(im1, 2) && y_orig >= 1 && y_orig <= size(im1, 1)
            % Assign the pixel value from the original image to the warped image
            warped_image(i, j, :) = im1(y_orig, x_orig, :);
        end
    end
end

% Display the warped image
figure;
imshow(warped_image / 255);
title('Warped Image using Nearest Neighbor Interpolation');

% Overlay the warped image with the second image for comparison
figure;
imshowpair(im2 / 255, warped_image / 255, 'blend');
title('Overlay of Image 2 and Warped Image 1 with Nearest Neighbor Interpolation')