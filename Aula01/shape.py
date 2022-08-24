import cv2 as cv
import numpy as np

image = cv.imread("../images/batman.png")

#                       Y   X
print("Pixel 138x196: ", image[196,138] )
h, w, bpp = np.shape(image)
print("Altura: ", h)
print("Largura: ", w)
print("bits por pixel (bpp): ", bpp)

preto = np.array([0,0,0])
azul = np.array([196, 161, 26])

for x in range(0,w):
    for y in range (0,h):
        if np.array_equal(image[y,x],preto):
            image[y,x] = azul

cv.imshow("Imagem", image)
cv.waitKey(0)
cv.destroyAllWindows()