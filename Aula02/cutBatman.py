import cv2 as cv

image = cv.imread('../images/batman.png')
roi =  image[150:220, 60:180]

# cv.imshow("Batman", image)
cv.imshow("Batman", roi)

cv.waitKey(0)
cv.destroyAllWindows()