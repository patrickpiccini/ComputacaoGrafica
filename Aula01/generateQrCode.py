import qrcode, cv2
img = qrcode.make('https://imed.edu.br')
img.save('teste.jpg')
image = cv2.imread("teste.jpg")
cv2.imshow("QRCODE", image)
cv2.waitKey(0)
cv2.destroyAllWindows()