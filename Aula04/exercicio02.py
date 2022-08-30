import cv2 as cv
import numpy as np


image = cv.imread('../images/plantas.jpg')
height, width, bpp = np.shape(image)

red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
black = (0,0,0)


# DO RECTANGLE
cv.rectangle(image, (92,303),(165,386), red, 2)
cv.rectangle(image, (185,223),(259,386), green, 2)
cv.rectangle(image, (266,215),(448,386), blue, 2)
cv.rectangle(image, (432,175),(719,386), black, 2)

cv.imshow("brain", image)

cv.waitKey(0)
cv.destroyAllWindows()


