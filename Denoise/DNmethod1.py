import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt

def main():
    filename = 'output_image_deblurred.jpg'
    img = cv2.imread(filename)

    # 38,38 for the trial 1
    
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    #void fastNlMeansDenoisingColored(InputArray src, OutputArray dst, float h=3, float hColor=3, int templateWindowSize=7, int searchWindowSize=21 )

    cv2.imwrite('denoised_' + filename, dst)

    #plt.subplot(121),plt.imshow(img)
    #plt.subplot(122),plt.imshow(dst)
    #plt.show()

if (__name__ == "__main__"):
    main()
