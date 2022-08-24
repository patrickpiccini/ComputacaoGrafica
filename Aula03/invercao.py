import cv2 as cv
import numpy as np

image = cv.imread('../images/cargo_ship_resize.jpg')
height, width, bpp = np.shape(image)

red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
white = (255,255,255)

# FLIP ON HAND
image1 = image[:,::-1]  # vertical
image2 = image[::-1,:]  # horizontal

# cv.imshow("cargo1", image1)
# cv.imshow("cargo2", image2)

fliped = cv.flip(image,0)
cv.imshow("cargo", fliped)



cv.waitKey(0)
cv.destroyAllWindows()