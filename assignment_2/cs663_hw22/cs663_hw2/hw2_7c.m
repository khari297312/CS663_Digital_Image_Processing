% Load the images
barbara = imread('barbara256.png');
kodak = imread('kodak24.png');

% Convert the images to double for adding noise
barbara = im2double(barbara);
kodak = im2double(kodak);

% Define the bilateral filter parameters
sigma_s1 = 2; sigma_r1 = 2/255;  % (σs = 2, σr = 2)
sigma_s2 = 0.1; sigma_r2 = 0.1/255;  % (σs = 0.1, σr = 0.1)
sigma_s3 = 3; sigma_r3 = 15/255;  % (σs = 3, σr = 15)

%after adding gaussian noise where sigma=10
% Add zero-mean Gaussian noise with standard deviation σ = 10
sigma = 10 / 255;  % Standard deviation should be normalized for imnoise
barbara_noisy = imnoise(barbara, 'gaussian', 0, sigma^2);
kodak_noisy = imnoise(kodak, 'gaussian', 0, sigma^2);


% Apply bilateral filter to the noisy images with different parameters
barbara_filtered1 = mybilateralfilter(barbara_noisy, sigma_r1, sigma_s1);
barbara_filtered2 = mybilateralfilter(barbara_noisy, sigma_r2, sigma_s2);
barbara_filtered3 = mybilateralfilter(barbara_noisy, sigma_r3, sigma_s3);

kodak_filtered1 = mybilateralfilter(kodak_noisy, sigma_r1, sigma_s1);
kodak_filtered2 = mybilateralfilter(kodak_noisy, sigma_r2, sigma_s2);
kodak_filtered3 = mybilateralfilter(kodak_noisy, sigma_r3, sigma_s3);

% Display the filtered results for Barbara
figure;
subplot(1, 3, 1), imshow(barbara_filtered1), title('(σs = 2, σr = 2)');
subplot(1, 3, 2), imshow(barbara_filtered2), title('(σs = 0.1, σr = 0.1)');
subplot(1, 3, 3), imshow(barbara_filtered3), title('(σs = 3, σr = 15)');

% Display the filtered results for Kodak
figure;
subplot(1, 3, 1), imshow(kodak_filtered1), title('(σs = 2, σr = 2)');
subplot(1, 3, 2), imshow(kodak_filtered2), title('(σs = 0.1, σr = 0.1)');
subplot(1, 3, 3), imshow(kodak_filtered3), title('(σs = 3, σr = 15)');