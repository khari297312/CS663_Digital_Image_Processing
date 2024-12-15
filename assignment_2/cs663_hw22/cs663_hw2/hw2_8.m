%Load the images:
LC1 = imread('LC1.png');
LC2 = imread('LC2.jpg');

%Apply local histogram equalization (Adaptive Histogram Equalization): Use different window sizes (7×7, 31×31, 51×51, 71×71):
LC1_local_7 = adapthisteq(LC1, 'NumTiles', [7 7]);
LC1_local_31 = adapthisteq(LC1, 'NumTiles', [31 31]);
LC1_local_51 = adapthisteq(LC1, 'NumTiles', [51 51]);
LC1_local_71 = adapthisteq(LC1, 'NumTiles', [71 71]);

LC2_local_7 = adapthisteq(LC2, 'NumTiles', [7 7]);
LC2_local_31 = adapthisteq(LC2, 'NumTiles', [31 31]);
LC2_local_51 = adapthisteq(LC2, 'NumTiles', [51 51]);
LC2_local_71 = adapthisteq(LC2, 'NumTiles', [71 71]);

%Apply global histogram equalization:
LC1_global = histeq(LC1);
LC2_global = histeq(LC2);


% For LC1
figure;
imshow(LC1), title('LC1 Original');

figure;
imshow(LC1_global), title('LC1 Global Equalization');

figure;
imshow(LC1_local_7), title('LC1 Local (7x7)');

figure;
imshow(LC1_local_31), title('LC1 Local (31x31)');

figure;
imshow(LC1_local_51), title('LC1 Local (51x51)');

% For LC2
figure;
imshow(LC2), title('LC2 Original');

figure;
imshow(LC2_global), title('LC2 Global Equalization');

figure;
imshow(LC2_local_7), title('LC2 Local (7x7)');

figure;
imshow(LC2_local_31), title('LC2 Local (31x31)');

figure;
imshow(LC2_local_51), title('LC2 Local (51x51)');

%{
figure;
subplot(1, 5, 1), imshow(LC1), title('LC1 Original');
subplot(1, 5, 2), imshow(LC1_global), title('LC1 Global Equalization');
subplot(1, 5, 3), imshow(LC1_local_7), title('LC1 Local (7x7)');
subplot(1, 5, 4), imshow(LC1_local_31), title('LC1 Local (31x31)');
subplot(1, 5, 5), imshow(LC1_local_51), title('LC1 Local (51x51)');

figure;
subplot(1, 5, 1), imshow(LC2), title('LC2 Original');
subplot(1, 5, 2), imshow(LC2_global), title('LC2 Global Equalization');
subplot(1, 5, 3), imshow(LC2_local_7), title('LC2 Local (7x7)');
subplot(1, 5, 4), imshow(LC2_local_31), title('LC2 Local (31x31)');
subplot(1, 5, 5), imshow(LC2_local_51), title('LC2 Local (51x51)');
%}



