from PIL import Image, ImageEnhance 

def main():

    filename = 'dog.jpg'
    image = Image.open(filename)
    size = width, height = image.size

    # Brightness, Contrast, Sharpness, Color

    enhancer = ImageEnhance.Sharpness (image)
    image = enhancer.enhance(85.0)

    #enhancer = ImageEnhance.Contrast (image)
    #image = enhancer.enhance(1.3)

    image.save ("deblurred_" + filename)
    del image

if (__name__ == "__main__"):
    main()
