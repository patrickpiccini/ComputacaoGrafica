import cv2 as cv
import numpy as np

coresIdentificadas = []
RANGE_COR = 50

image = cv.imread("../images/venezuela.png")

altura, largura, bpp = np.shape(image)

for y in range(0, altura):
    for x in range(0, largura):
        pixel = image[y,x]
        pixelArray = [pixel[0], pixel[1], pixel[2]] 
        if pixelArray not in coresIdentificadas:
            coresIdentificadas.append(pixelArray)

print("Cores identificadas")

for i, cor in enumerate(coresIdentificadas):
    print(f"\t{i+1}° - {cor[0]}, {cor[1]}, {cor[2]}")