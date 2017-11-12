import cv2
import numpy as np
from scipy.misc import imread, imsave, imshow
from PIL import Image 

filename = '[DOPE]motion-deblurred-noise.jpg'
image = imread(filename, flatten = True)

# 1. Add noises to the image
noisy1 = image + image.std() * np.random.random(image.shape)

alot  = image.max() * np.random.random(image.shape)
noisy2 = image + 0.1*alot

cv2.imwrite("noise.jpg", noisy2)
