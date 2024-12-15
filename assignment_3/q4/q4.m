% Step 1: Create a 201x201 image with a bright central column
image_size = 201;
image = zeros(image_size, image_size);  % Initialize a black 201x201 image
image(:, 101) = 255;  % Set the central column (column 101) to have pixel value 255

% Step 2: Compute the 2D Discrete Fourier Transform using fft2
F = fft2(image);

% Step 3: Shift the zero-frequency component to the center of the spectrum
F_shifted = fftshift(F);

% Step 4: Compute the magnitude of the Fourier transform
F_magnitude = abs(F_shifted);

% Step 5: Take the logarithm of the magnitude for better visualization
F_log_magnitude = log(F_magnitude + 1);  % Add 1 to avoid log(0)

% Step 6: Display the Fourier magnitude
figure;
imagesc(F_log_magnitude);  % Display the log-magnitude as an image
colorbar;  % Add a colorbar for reference
title('Log Magnitude of the Discrete Fourier Transform');
xlabel('Frequency u');
ylabel('Frequency v');
axis image;  % Ensure the aspect ratio is correct
