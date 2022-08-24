import cv2 as cv
import numpy as np

image = cv.imread('../images/batman.png')
roi =  image[150:220, 60:180]

# cv.imshow("Batman", roi)

heigth, width, bpp = np.shape(roi)

resize_as = cv.resize(roi,(5*width, 5*heigth), interpolation=cv.INTER_CUBIC)

cv.imshow("Batman", resize_as)

cv.waitKey(0)
cv.destroyAllWindows()