import cv2 as cv
import numpy as np

white = 255
coresIdentificadas = 0
coresTotal = 0

image = cv.imread("../images/sojafalhas.jpg")

altura, largura, bpp = np.shape(image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
(_, bin ) = cv.threshold(gray,160,255,cv.THRESH_BINARY)


for y in range(0, altura):
	for x in range(0, largura):
		if bin[y,x] == white:
			coresIdentificadas += 1
		coresTotal +=1

percent = (coresIdentificadas * 100) / coresTotal

print(f"""\
Plantação falha: {percent:.2f}%
Plantação Saldavel: {(100-percent):.2f}%
"""
)

cv.imshow("Imagem", bin)
cv.waitKey(0)
cv.destroyAllWindows()