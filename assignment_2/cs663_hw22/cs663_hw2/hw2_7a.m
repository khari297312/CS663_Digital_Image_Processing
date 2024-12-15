% Load the images
barbara = imread('barbara256.png');
kodak = imread('kodak24.png');

% Convert the images to double for adding noise
barbara = im2double(barbara);
kodak = im2double(kodak);

% Add zero-mean Gaussian noise with standard deviation σ = 5
sigma = 5 / 255;  % Standard deviation should be normalized for imnoise
barbara_noisy = imnoise(barbara, 'gaussian', 0, sigma^2);
kodak_noisy = imnoise(kodak, 'gaussian', 0, sigma^2);

% Display the noisy images
figure;
subplot(121),imshow(barbara), title('Original Image');
subplot(122),imshow(barbara_noisy), title('After adding Gaussian Noise (σ = 5)');

figure;
subplot(121),imshow(kodak), title('Original Image');
subplot(122),imshow(kodak_noisy), title('After adding Gaussian Noise (σ = 5)');