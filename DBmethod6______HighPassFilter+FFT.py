import cv2
import numpy as np
from matplotlib import pyplot as plt
import scipy.misc

img = cv2.imread('dog.jpg',0)

# fft to convert the image to freq domain 
f = np.fft.fft2(img)

# shift the center
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)


# remove the low frequencies by masking with a rectangular window of size 60x60
# High Pass Filter (HPF)
fshift[crow-1:crow+1, ccol-1:ccol+1] = 0

# shift back (we shifted the center before)
f_ishift = np.fft.ifftshift(fshift)

# inverse fft to get the image back 
img_back = np.fft.ifft2(f_ishift)

img_back = np.abs(img_back)

scipy.misc.imsave('sixtrial.jpg', img_back)
