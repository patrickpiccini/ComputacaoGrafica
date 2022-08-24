
import cv2 as cv
import numpy as np

COR_PRETA = np.array([0, 0, 0])
COR_MENOR = np.array([0, 15, 15])
COR_MAIOR = np.array([177, 82, 104])

image = cv.imread("../images/camisagarrincha.jpg")

hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
blur = cv.medianBlur(hsv, 7)

maks = cv.inRange(blur, COR_MENOR, COR_MAIOR)

imageWithMask = cv.bitwise_and(image, image, mask=maks)

altura, largura, bpp = np.shape(image)

for y in range(0, altura):
    for x in range(0, largura):
        if(not np.array_equal(imageWithMask[y,x], COR_PRETA)):
            image[y,x] = np.array([49, 22, 222])


cv.imshow("Imagem com cor trocada", image)
cv.waitKey(0)
cv.destroyAllWindows()

