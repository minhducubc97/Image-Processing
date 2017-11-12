# Deblurring-Blurring-AddingNoise

As part of my work for UBC Orbit Payload Team, I have to do research on deblurring/blurring, adding/removing noise from images and program them in Python. The eventual goal is to get a clear image from the camera installed on our design team satelitte.

As for the required library, I use a mixture of OpenCV, Scipy and PIL

Below are the list of methods that deblur/blur, add/remove noise from images that I have done research on:

1) Deblurring (The methods below don't not require a specific kernel to deblur, all one has to do is to adjust the key variable to get a desired effect):
a) ImageEnhance
b) Richard-Lucy 
c) Wiener
d) High pass filter (built-in function)
e) High pass filter with Fourier transform
f) Unsharp [This one for me gives the best result]
  
2) Denoising:
a) fastNlMeansDenoisingColored (OpenCV built-in function)
b) Customized denoise function [This one for me gives the best result]
  
3) Adding noise:
a) Random noise
  
3) Deblurring/Blurring with a specific kernel:
a) Gaussian kernel
b) Motion kernel
