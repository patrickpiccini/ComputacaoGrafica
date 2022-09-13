from email.mime import image
import cv2 as cv
import mahotas
import numpy as np
imagem = cv.imread('images/futebol1.jpg')

cv.imshow("Imagem", imagem)


'''
# Método por limiar
gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
limiar = 150
(_, bin ) = cv.threshold(gray,limiar,255,cv.THRESH_BINARY)
cv.imshow("Limiar", bin)
'''

'''
# Método por Adaptativo

gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
suave = cv.GaussianBlur(gray, (7, 7), 0)
cv.imshow("Suave", suave)
bin1 = cv.adaptiveThreshold(
    suave, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 5)
cv.imshow("Bin1", bin1)

bin2 = cv.adaptiveThreshold(
    suave, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 21, 5)
cv.imshow("Bin2", bin2)
'''

'''
# Método por Otsu e Riddler
# pip install mahotas


gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
suave = cv.GaussianBlur(gray, (7, 7), 5)

limiar = mahotas.thresholding.otsu(suave)

otsu = gray.copy()
otsu[otsu > limiar] = 255
otsu[otsu < 255] = 0
#otsu = cv.bitwise_not(otsu)
cv.imshow("Otsu",otsu)

limiar = mahotas.thresholding.rc(suave)
rc = gray.copy()
rc[rc > limiar] = 255
rc[rc < 255] = 0
rc = cv.bitwise_not(rc)
cv.imshow("Riddler",rc)
'''
'''
# Método por Sobel

gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
cv.imshow("Sobel X", sobelX)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
cv.imshow("Sobel Y", sobelY)
sobel = cv.bitwise_and(sobelX, sobelY)
cv.imshow("Sobel", sobel)
'''
'''
# Método por Laplaciano
gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
laplaciano = cv.Laplacian(gray, cv.CV_64F)
laplaciano= np.uint8(np.absolute(laplaciano))
cv.imshow("Laplaciano", laplaciano)
'''

# Método por Canny
gray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)
suave = cv.GaussianBlur(gray, (7,7), 0)
canny = cv.Canny(suave, 70,200)

cv.imshow("Canny", canny)

cv.waitKey(0)
cv.destroyAllWindows()
