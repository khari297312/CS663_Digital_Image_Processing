% Load images
im1 = imread('goi1.jpg');
im2 = imread('goi2.jpg');

% Convert images to double precision
im1 = double(im1);
im2 = double(im2);

% Assume problem6_a_matrix is already generated from the previous step
% Here it's just a placeholder; replace it with your actual matrix
% problem6_a_matrix = [Your generated matrix here];

% Get the dimensions of the second image (output image)
[rows, cols, channels] = size(im2);

% Initialize the output (warped) image
warped_image = zeros(rows, cols, channels);

% Invert the affine transformation matrix for backward warping
inv_matrix = inv(problem6_a_matrix);

% Perform bilinear interpolation
for i = 1:rows
    for j = 1:cols
        % Apply the inverse affine transformation to map output (warped) coordinates to input (im1) coordinates
        original_coords = inv_matrix * [j; i; 1];
        
        % Extract the original x and y coordinates
        x_orig = original_coords(1);
        y_orig = original_coords(2);
        
        % Find the integer coordinates of the four nearest neighbors
        x1 = floor(x_orig);
        y1 = floor(y_orig);
        x2 = ceil(x_orig);
        y2 = ceil(y_orig);
        
        % Check if the coordinates are within the bounds of the image
        if x1 >= 1 && x1 < size(im1, 2) && y1 >= 1 && y1 < size(im1, 1)
            % Get pixel values for the four neighboring pixels
            Q11 = im1(y1, x1, :);
            Q12 = im1(y1, x2, :);
            Q21 = im1(y2, x1, :);
            Q22 = im1(y2, x2, :);
            
            % Compute weights for bilinear interpolation
            alpha = x_orig - x1;
            beta = y_orig - y1;
            
            % Compute the interpolated value
            top = (1 - alpha) * Q11 + alpha * Q12;
            bottom = (1 - alpha) * Q21 + alpha * Q22;
            warped_image(i, j, :) = (1 - beta) * top + beta * bottom;
        end
    end
end

% Display the warped image
figure;
imshow(warped_image / 255);
title('Warped Image using Bilinear Interpolation');

% Overlay the warped image with the second image for comparison
figure;
imshowpair(im2 / 255, warped_image / 255, 'blend');
title('Overlay of Image 2 and Warped Image 1 with Bilinear Interpolation');
