% Load original images
im1 = imread('goi1.jpg'); % Original image 1
im2 = imread('goi2.jpg'); % Original image 2

% Convert images to double precision
im1 = double(im1);
im2 = double(im2);

% Initialize arrays to store the points
x1 = zeros(1, 12);
y1 = zeros(1, 12);
x2 = zeros(1, 12);
y2 = zeros(1, 12);

% Manually select 12 pairs of corresponding points
for i = 1:12
    % Select point from the first image
    figure(1);
    imshow(im1 / 255);
    title(sprintf('Select point %d from Image 1', i));
    [x1(i), y1(i)] = ginput(1);
    
    % Select corresponding point from the second image
    figure(2);
    imshow(im2 / 255);
    title(sprintf('Select corresponding point %d from Image 2', i));
    [x2(i), y2(i)] = ginput(1);
end

% Prepare new images for annotation
new_image1 = im1;
new_image2 = im2;

% Annotate new_image1 with control points
figure;
imshow(new_image1 / 255); % Display image with normalization
title('Control Points on New Image 1');
hold on;
for i = 1:length(x1)
    plot(x1(i), y1(i), 'ro', 'MarkerSize', 8, 'LineWidth', 2);
    text(x1(i), y1(i), num2str(i), 'Color', 'yellow', 'FontSize', 12, 'FontWeight', 'bold');
end
hold off;

% Annotate new_image2 with control points
figure;
imshow(new_image2 / 255); % Display image with normalization
title('Control Points on New Image 2');
hold on;
for i = 1:length(x2)
    plot(x2(i), y2(i), 'go', 'MarkerSize', 8, 'LineWidth', 2);
    text(x2(i), y2(i), num2str(i), 'Color', 'cyan', 'FontSize', 12, 'FontWeight', 'bold');
end
hold off;

% Prepare the points for the affine transformation estimation
movingPoints = [x2', y2']; % Points from the second image
fixedPoints = [x1', y1'];  % Corresponding points from the first image

% Estimate the affine transformation matrix
tform = fitgeotrans(movingPoints, fixedPoints, 'affine');

% Extract the affine transformation matrix
problem6_a_matrix = tform.T; % 3x3 affine transformation matrix

% Display the matrix
disp('Affine Transformation Matrix (problem6_a_matrix):');
disp(problem6_a_matrix);

% Apply the transformation to align the second image with the first
alignedImage = imwarp(im2 / 255, tform, 'OutputView', imref2d(size(im1)));

% Display the aligned image
figure;
imshow(alignedImage);
title('Aligned Image');

% Overlay the aligned image with the first image to visualize the transformation
figure;
imshowpair(im1 / 255, alignedImage, 'blend');
title('Overlay of Image 1 and Aligned Image 2');
