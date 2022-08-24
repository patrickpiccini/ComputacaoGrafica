import cv2 as cv
import numpy as np

# deve ser executado na pasta computacaoGrafica
image = cv.imread("../images/venezuela.png")

height, width, bpp = np.shape(image)
print("Altura: ", height)
print("Largura: ", width)
print("bits por pixel (bpp): ", bpp)


def analisaLimiar(lista, cor, limiar):
    retorno = True
    if len(lista) == 0:
        return True
    else:
        for corIndex in lista:
            corB = corIndex[0]
            corBMin = corB - limiar
            corBmax = corB + limiar
            corG = corIndex[1]
            corGMin = corG - limiar
            corGMax = corG + limiar
            corR = corIndex[2]
            corRMin =corR - limiar
            corRMax = corR + limiar
            if cor[0] >= corBMin and cor[0]<= corBmax:
                if cor[1] >= corGMin and cor[1]<= corGMax:
                    if cor[2] >= corRMin and cor[2]<=corRMax:
                        retorno = False
    return retorno            


listaCores = []
limiar = 140
for y in range(0,height):
    for x in range(0, width):
        cor = list(image[y,x])
        if not cor in listaCores:
            if analisaLimiar(listaCores, cor, limiar):
                listaCores.append(cor)

print("Nº de cores:", len(listaCores))
print("Cores:", listaCores)

cv.imshow("Imagem", image)
cv.waitKey(0)
cv.destroyAllWindows()