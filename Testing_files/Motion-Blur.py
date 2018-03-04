from Detectblur import detect_blur
from Blurrer import LineKernel, SanitizeAngleValue, nearestValue

import cv2
import numpy as np
from scipy.ndimage.filters import convolve
from scipy.misc import imread, imsave
from PIL import Image

import math
from scipy.signal import convolve2d
from skimage.draw import line

from LineDictionary import LineDictionary

image = imread("trial_earth.jpg", flatten=True)

# generating the kernel
kernel = LineKernel(7, 180, 'right')

# Pad kernel (make the kernel has the same shape as the image)
l = np.zeros_like(image)
l[:kernel.shape[0],:kernel.shape[1]] = kernel
kernel = l
imsave('Original_kernel.jpg', kernel)

# Normalize values (0,255)->(0,1)
image = image/np.max(image)
image_fft = (np.fft.fft2(image))
kernel_fft = (np.fft.fft2(kernel))

# Blur
blurred_array = np.multiply(image_fft, kernel_fft**7) # add power to kernel_fft to get more motion applied to the image
blurred_array_shift = np.fft.fftshift( blurred_array )
blurred_array = np.fft.ifft2(blurred_array)
# Save
blurred_image = Image.fromarray( 255*(np.abs(blurred_array)/np.max(blurred_array)).real).convert('RGB').save('[DOPE]motion-blurred.jpg')
deblurred_image = Image.fromarray( 255*(np.abs(blurred_array)/np.max(blurred_array)).real).convert('RGB').save('[DOPE]motion-deblurred.jpg')

status, degree_of_blur = detect_blur("[DOPE]motion-deblurred.jpg")
flag = 1
deblurred_array = np.fft.fft2( blurred_array )
var = 3
exp = 1

while (status != "Good"):
    if (status == "Distorted"):
        deblurred_array = deblurred_array_backup
        deblurred_image = Image.fromarray( 255*(np.abs(deblurred_array)/np.max(deblurred_array)).real).convert('RGB').save('[DOPE]motion-deblurred.jpg')
        kernel_fft = (kernel_fft)**(1/(var**exp))
        exp = exp + 1
    deblurred_array_backup = deblurred_array
    if (flag == 1):
        flag = 0
    else:
        deblurred_array = np.fft.fft2( deblurred_array )
    deblurred_array = np.divide( deblurred_array, kernel_fft )
    deblurred_array = np.fft.ifft2( deblurred_array )
    deblurred_image = Image.fromarray( 255*(np.abs(deblurred_array)/np.max(deblurred_array)).real).convert('RGB').save('[DOPE]motion-deblurred.jpg')
    status, degree_of_blur = detect_blur("[DOPE]motion-deblurred.jpg")
    print (status)

## NOT WORKING - Training program
##while (status != "Good"):
##    if (status == "Distorted"):
##        deblurred_array = deblurred_array_backup
##        kernel_fft = kernel_fft**0.5
##    deblurred_array_backup = deblurred_array
##    if (flag == 1):
##        flag = 0
##    else:
##        deblurred_array = np.fft.fft2( deblurred_array )
##    deblurred_array = np.divide( deblurred_array, kernel_fft )
##    deblurred_array = np.fft.ifft2( deblurred_array )
##    deblurred_image = Image.fromarray( 255*(np.abs(deblurred_array)/np.max(deblurred_array)).real).convert('RGB').save('[DOPE]motion-deblurred.jpg')
##    status, degree_of_blur = detect_blur("[DOPE]motion-deblurred.jpg")
##    print (status)
