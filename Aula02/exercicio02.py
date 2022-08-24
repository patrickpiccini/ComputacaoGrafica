import cv2 as cv

image = cv.imread('../images/simpsons.jpg')
#              Y         X
roi =  image[0:1400, 400:1350]

cv.imshow("Homer", roi)

cv.waitKey(0)
cv.destroyAllWindows()