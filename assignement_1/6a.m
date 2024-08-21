% Load images
im1 = imread('goi1.jpg');
im2 = imread('goi2.jpg');

% Cast images to double
im1 = double(im1);
im2 = double(im2);

% Display the first image
figure(1);
imshow(im1/255); % Dividing by 255 to normalize the image for display

% Display the second image
figure(2);
imshow(im2/255); % Dividing by 255 to normalize the image for display

% Initialize arrays to store the points
x1 = zeros(1, 12);
y1 = zeros(1, 12);
x2 = zeros(1, 12);
y2 = zeros(1, 12);

% Manually select points
for i = 1:12
    figure(1);
    imshow(im1/255);
    [x1(i), y1(i)] = ginput(1); % Select a point on the first image
    
    figure(2);
    imshow(im2/255);
    [x2(i), y2(i)] = ginput(1); % Select the corresponding point on the second image
end

% Prepare the points as required by fitgeotrans
movingPoints = [x2', y2']; % Points from the second image
fixedPoints = [x1', y1'];  % Corresponding points from the first image

% Estimate the affine transformation
tform = fitgeotrans(movingPoints, fixedPoints, 'affine');

% Apply the transformation to align the second image with the first
outputImage = imwarp(im2/255, tform, 'OutputView', imref2d(size(im1)));

% Display the aligned image
figure;
imshow(outputImage);
title('Aligned Image');
