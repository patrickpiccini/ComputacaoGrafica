import cv2 as cv

imagem  = cv.imread("../images/j.png")

cv.imshow("img", imagem)

cv.waitKey(0)
cv.destroyAllWindows()