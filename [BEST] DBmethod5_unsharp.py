import cv2

image = cv2.imread("dog.jpg")
gaussian_3 = cv2.GaussianBlur(image, (9,9), 10.0)
unsharp_image = cv2.addWeighted(image, 8, gaussian_3, -7, 0, image)
cv2.imwrite("dog_unsharp.jpg", unsharp_image)
