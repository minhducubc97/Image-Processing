import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image
import scipy.misc

# Load the data...
im = Image.open('dog.jpg')
data = np.array(im, dtype=float)

im2 = Image.open('deblurred_dog.jpg')
data2 = np.array(im2, dtype=float)

im3 = Image.open('sixtrial.jpg')
data3 = np.array(im, dtype=float)

# Another way of making a highpass filter is to simply subtract a lowpass
# filtered image from the original. Here, we'll use a simple gaussian filter
# to "blur" (i.e. a lowpass filter) the original.
lowpass = ndimage.gaussian_filter(data2, 10)
gauss_highpass = data2 - lowpass

out = data*0.3 + gauss_highpass*0.35 + (data2 - lowpass)*0.2 + data3*0.15

scipy.misc.imsave('deblur.jpg', out)

