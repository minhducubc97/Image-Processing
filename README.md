# Deblurring-Blurring-AddingNoise

As part of my work for UBC Orbit Payload Team, I have to do research on deblurring/blurring, adding/removing noise from images and program them in Python. The eventual goal is to get a clear image from the camera installed on our design team satelitte.

As for the required library, I use a mixture of OpenCV, Scipy and PIL

Below are the list of methods that deblur/blur, add/remove noise from images that I have done research on:

1) Deblurring (The methods below don't not require a specific kernel to deblur, all one has to do is to adjust the key variable to get a desired effect):
- ImageEnhance
- Richard-Lucy 
- Wiener
- Gaussian High pass filter (built-in function)
- High pass filter with Fourier transform
- Unsharp [This one for me gives the best result]
  
2) Denoising:
- fastNlMeansDenoisingColored (OpenCV built-in function)
- Customized denoise function [This one for me gives the best result]
  
3) Adding noise:
- Random noise
  
3) Deblurring/Blurring with a specific kernel:
- Gaussian kernel
- Motion kernel
