import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('../images/lordoftherings.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
equalize = cv.equalizeHist(gray)
image = cv.calcHist([image], [0], None, [256], [0,256])
betterImage = cv.calcHist([equalize], [0], None, [256], [0,256])

cv.imshow('img', gray)
cv.imshow('equalize', equalize)
plt.figure()
plt.title('Histograma')
plt.xlabel('Intensidade')
plt.ylabel('Qtde. Pixel')
plt.xlim([0,256])
plt.plot(image)

plt.figure()
plt.plot(betterImage)


plt.show()

cv.waitKey(0)
cv.destroyAllWindows()