import cv2 as cv

image = cv.imread('../images/estrada.png')

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Estrada", image)
cv.imshow("gray",gray)

(_, bin ) = cv.threshold(gray,160,255,cv.THRESH_BINARY)

cv.imshow("Binaria", bin)

cv.waitKey(0)
cv.destroyAllWindows()