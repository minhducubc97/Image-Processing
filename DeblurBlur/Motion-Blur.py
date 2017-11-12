import cv2
import numpy as np
from scipy.ndimage.filters import convolve
from scipy.misc import imread, imsave
from PIL import Image

import math
from scipy.signal import convolve2d
from skimage.draw import line

from LineDictionary import LineDictionary

lineLengths =[3,5,7,9]
lineTypes = ["full", "right", "left"]

lineDict = LineDictionary()

def LineKernel(dim, angle, linetype):
    kernelwidth = dim
    kernelCenter = int(math.floor(dim/2))
    angle = SanitizeAngleValue(kernelCenter, angle)
    kernel = np.zeros((kernelwidth, kernelwidth), dtype=np.float32)
    lineAnchors = lineDict.lines[dim][angle]
    if(linetype == 'right'):
        lineAnchors[0] = kernelCenter
        lineAnchors[1] = kernelCenter
    if(linetype == 'left'):
        lineAnchors[2] = kernelCenter
        lineAnchors[3] = kernelCenter
    rr,cc = line(lineAnchors[0], lineAnchors[1], lineAnchors[2], lineAnchors[3])
    kernel[rr,cc]=1
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor        
    return kernel

def SanitizeAngleValue(kernelCenter, angle):
    numDistinctLines = kernelCenter * 4
    angle = math.fmod(angle, 180.0)
    validLineAngles = np.linspace(0,180, numDistinctLines, endpoint = False)
    angle = nearestValue(angle, validLineAngles)
    return angle

def nearestValue(theta, validAngles):
    idx = (np.abs(validAngles-theta)).argmin()
    return validAngles[idx]

image = imread("trial_earth.jpg", flatten=True)

# generating the kernel
kernel = LineKernel(7, 180, 'right')

# Pad kernel (make the kernel has the same shape as the image)
l = np.zeros_like(image)
l[:kernel.shape[0],:kernel.shape[1]] = kernel
kernel = l

# Normalize values (0,255)->(0,1)
image = image/np.max(image)
image_fft = (np.fft.fft2(image))
kernel_fft = (np.fft.fft2(kernel))

# Blur
blurred_array = np.multiply(image_fft, kernel_fft) # add power to kernel_fft to get more motion applied to the image
blurred_array_shift = np.fft.fftshift( blurred_array )
blurred_array = np.fft.ifft2(blurred_array)

# Deblur
deblurred_array = np.fft.fft2( blurred_array )
deblurred_array_fft = np.fft.fftshift( deblurred_array )
deblurred_array = np.divide( deblurred_array, kernel_fft )
deblurred_array = np.fft.ifft2( deblurred_array )

# Save
blurred_image = Image.fromarray( 255*(np.abs(blurred_array)/np.max(blurred_array)).real).convert('RGB').save('[DOPE]motion-blurred.jpg')
deblurred_image = Image.fromarray( 255*(np.abs(deblurred_array)/np.max(deblurred_array)).real).convert('RGB').save('[DOPE]motion-deblurred.jpg')

