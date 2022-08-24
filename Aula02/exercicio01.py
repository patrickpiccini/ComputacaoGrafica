import cv2 as cv

image = cv.imread('../images/simpsons.jpg')
#                Y         X
roi =  image[450:900, 1360:1680]

cv.imshow("Bart", roi)
cv.imwrite('Bart.png', roi)

cv.waitKey(0)
cv.destroyAllWindows()