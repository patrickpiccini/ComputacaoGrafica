import cv2 as cv
import numpy as np

image = cv.imread('../images/estrada.png')
height, width, bpp = np.shape(image)
cv.imshow("image",image)
print(image[10,10])

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
print(gray[10,10])

hvs = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("hvs",hvs)
print(hvs[10,10])

lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)
print(lab[10,10])


cv.waitKey(0)
cv.destroyAllWindows()