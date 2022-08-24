import cv2 as cv
import numpy as np

image = cv.imread("../images/camisagarrincha.jpg")

h, w, bpp = np.shape(image)

preto = np.array([0,0,0])
outro = np.array([124, 131, 56])

for x in range(0,w):
    for y in range (0,h):
        if np.array_equal(image[y,x],preto):
            image[y,x] = outro

cv.imshow("Imagem", image)
cv.waitKey(0)
cv.destroyAllWindows()