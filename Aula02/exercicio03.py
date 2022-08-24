import cv2 as cv
from PIL import Image 

image = cv.imread('../images/simpsons.jpg')
#                Y         X
roi =  image[950:1550, 2179:2450]

inverter = cv.flip(roi, 0)
cv.imshow("Lisa", inverter)

cv.waitKey(0)
cv.destroyAllWindows()