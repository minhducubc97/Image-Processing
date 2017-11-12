import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image
import scipy.misc

# Load the data...
im = Image.open('dog.jpg')
data = np.array(im, dtype=float)

# Another way of making a highpass filter is to simply subtract a lowpass
# filtered image from the original. Here, we'll use a simple gaussian filter
# to "blur" (i.e. a lowpass filter) the original.
lowpass = ndimage.gaussian_filter(data, 10)
gauss_highpass = data - lowpass

out = data*0.5 + gauss_highpass*0.5

scipy.misc.imsave('deblur.jpg', out)

