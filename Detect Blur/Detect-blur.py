# import the necessary packages
from imutils import paths
import argparse
# The argparse module makes it easy to write user-friendly command-line interfaces. The program
# defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. 
import cv2

# define threshold
low_threshold = 350
high_threshold = 1000

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# load the image, convert it to grayscale, and compute the
# focus measure of the image using the Variance of Laplacian
# method
image = cv2.imread("dummy2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)
text = "Good"
 
# if the focus measure is less than the supplied threshold,
# then the image should be considered "blurry"
if fm < low_threshold:
    text = "Blurry"

elif fm > high_threshold:
    text = "Distorted"
 
# show the image
cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.imshow("Image", image)
key = cv2.waitKey(0)
