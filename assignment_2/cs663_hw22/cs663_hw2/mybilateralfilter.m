function B = mybilateralfilter(img, sigma_s, sigma_r)

    % Normalize image if not already in range [0, 1]
    if max(img(:)) > 1
        img = im2double(img);
    end

    % Define the window size based on sigma_s
    % Typically, width is set to ~3 * sigma_s to capture most of the filters influence
    width = ceil(3 * sigma_s);

    % Precompute Gaussian spatial weights
    [X, Y] = meshgrid(-width:width, -width:width);
    G = exp(-(X.^2 + Y.^2) / (2 * sigma_s^2));

    % Get image dimensions
    [rows, cols] = size(img);
    B = zeros(rows, cols);

    % Apply the bilateral filter
    for i = 1:rows
        for j = 1:cols
            % Extract local region
            iMin = max(i - width, 1);
            iMax = min(i + width, rows);
            jMin = max(j - width, 1);
            jMax = min(j + width, cols);
            I = img(iMin:iMax, jMin:jMax);

            % Compute range weights (difference in intensity)
            H = exp(-(I - img(i, j)).^2 / (2 * sigma_r^2));

            % Combine spatial and range weights
            F = H .* G((iMin:iMax) - i + width + 1, (jMin:jMax) - j + width + 1);

            % Calculate the output pixel value
            B(i, j) = sum(F(:) .* I(:)) / sum(F(:));
        end
    end
end
