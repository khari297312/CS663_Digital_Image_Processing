% Load the image
image = imread('barbara256.png');
image = double(image);

% Zero-padding to avoid boundary effects
pad_size = 256;
image_padded = padarray(image, [pad_size, pad_size], 'both');

% Perform Fourier Transform of the padded image
F = fft2(image_padded);
F_shifted = fftshift(F); % Shift zero frequency to the center

% Get padded image dimensions
[M, N] = size(image_padded);

% Create meshgrid for frequency domain
[u, v] = meshgrid(1:N, 1:M);
u = u - ceil(N/2); % Shift u to have zero in the center
v = v - ceil(M/2); % Shift v to have zero in the center
D_uv = sqrt(u.^2 + v.^2); % Distance matrix

% Parameters for cutoff frequencies and Gaussian sigma
cutoff1 = 40;
cutoff2 = 80;
sigma1 = 40;
sigma2 = 80;

% (a) Ideal Low Pass Filter (ILPF)
ideal_LPF_40 = double(D_uv <= cutoff1);
ideal_LPF_80 = double(D_uv <= cutoff2);

% (b) Gaussian Low Pass Filter (GLPF)
gaussian_LPF_40 = exp(-(D_uv.^2) / (2 * sigma1^2));
gaussian_LPF_80 = exp(-(D_uv.^2) / (2 * sigma2^2));

% Apply the filters in frequency domain
filtered_F_ideal_40 = F_shifted .* ideal_LPF_40;
filtered_F_ideal_80 = F_shifted .* ideal_LPF_80;
filtered_F_gaussian_40 = F_shifted .* gaussian_LPF_40;
filtered_F_gaussian_80 = F_shifted .* gaussian_LPF_80;

% Inverse Fourier Transform to get the filtered images
ideal_filtered_image_40 = real(ifft2(ifftshift(filtered_F_ideal_40)));
ideal_filtered_image_80 = real(ifft2(ifftshift(filtered_F_ideal_80)));
gaussian_filtered_image_40 = real(ifft2(ifftshift(filtered_F_gaussian_40)));
gaussian_filtered_image_80 = real(ifft2(ifftshift(filtered_F_gaussian_80)));

% Crop the images to remove padding
ideal_filtered_image_40 = ideal_filtered_image_40(pad_size+1:end-pad_size, pad_size+1:end-pad_size);
ideal_filtered_image_80 = ideal_filtered_image_80(pad_size+1:end-pad_size, pad_size+1:end-pad_size);
gaussian_filtered_image_40 = gaussian_filtered_image_40(pad_size+1:end-pad_size, pad_size+1:end-pad_size);
gaussian_filtered_image_80 = gaussian_filtered_image_80(pad_size+1:end-pad_size, pad_size+1:end-pad_size);

% (c) Log Absolute Fourier Transforms for Visualization
log_F_original = log(1 + abs(F_shifted));
log_F_ideal_40 = log(1 + abs(filtered_F_ideal_40));
log_F_ideal_80 = log(1 + abs(filtered_F_ideal_80));
log_F_gaussian_40 = log(1 + abs(filtered_F_gaussian_40));
log_F_gaussian_80 = log(1 + abs(filtered_F_gaussian_80));

% Display the frequency responses of the filters
figure;
subplot(2,2,1), imshow(log(1 + abs(ideal_LPF_40)), []), title('Ideal LPF, D=40 (Frequency Response)');
subplot(2,2,2), imshow(log(1 + abs(ideal_LPF_80)), []), title('Ideal LPF, D=80 (Frequency Response)');
subplot(2,2,3), imshow(log(1 + abs(gaussian_LPF_40)), []), title('Gaussian LPF, \sigma=40 (Frequency Response)');
subplot(2,2,4), imshow(log(1 + abs(gaussian_LPF_80)), []), title('Gaussian LPF, \sigma=80 (Frequency Response)');

% Display the log absolute Fourier transforms of the original and filtered images
figure;
subplot(2,3,1), imshow(log_F_original, []), title('Original Image (Log Fourier)');
subplot(2,3,2), imshow(log_F_ideal_40, []), title('Filtered (Ideal LPF, D=40)');
subplot(2,3,3), imshow(log_F_ideal_80, []), title('Filtered (Ideal LPF, D=80)');
subplot(2,3,4), imshow(log_F_gaussian_40, []), title('Filtered (Gaussian LPF, \sigma=40)');
subplot(2,3,5), imshow(log_F_gaussian_80, []), title('Filtered (Gaussian LPF, \sigma=80)');

% Display the filtered images in the spatial domain
figure;
subplot(2,3,1), imshow(uint8(image)), title('Original Image');
subplot(2,3,2), imshow(uint8(ideal_filtered_image_40)), title('Ideal LPF, D=40');
subplot(2,3,3), imshow(uint8(ideal_filtered_image_80)), title('Ideal LPF, D=80');
subplot(2,3,4), imshow(uint8(gaussian_filtered_image_40)), title('Gaussian LPF, \sigma=40');
subplot(2,3,5), imshow(uint8(gaussian_filtered_image_80)), title('Gaussian LPF, \sigma=80');
