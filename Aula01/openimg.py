import cv2 as cv
imagem = cv.imread("../images/clouds.jpg")
# arquivo = filedialog.askopenfilename(multiple=False)
# imagem = cv.imread(arquivo) 
imagemGray = cv.cvtColor(imagem, cv.COLOR_BGR2GRAY)


cv.imshow("Original",imagem)
cv.imshow("Gray Scale",imagemGray)

cv.waitKey(0)
cv.destroyAllWindows()