import cv2 as cv
import numpy as np


image = cv.imread('../images/brain1.jpg')
height, width, bpp = np.shape(image)

red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
white = (255,255,255)

# DO LINE
# cv.line(image, (0,100),(100,100), red, 5)

# DO RECTANGLE
# cv.rectangle(image, (50,100),(100,200), red, 2)

# DO CIRCLE
# (x,y) = (image.shape[1]//2, image.shape[0]//2)
# for raio in range(0,175,15):
# 	cv.circle(image, (x,y), raio, red, 2)

# WRITE TEXT
fonte = cv.FONT_HERSHEY_SIMPLEX
cv.putText(image, "Ultrassonografia", (50,50), fonte, 1, white, 2, cv.LINE_AA)

cv.imshow("brain", image)

cv.waitKey(0)
cv.destroyAllWindows()