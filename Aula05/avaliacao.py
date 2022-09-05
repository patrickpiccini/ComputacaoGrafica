import cv2 as cv
import numpy as np
import pyautogui

camera = cv.VideoCapture(0, cv.CAP_DSHOW)
sizeScreen = pyautogui.size()
x = y = w = h = 1
coldown = 0
stop = False

# RANGE DE CORES
lowerBlue = np.array([94,121,40])
upperBlue = np.array([137,250,255])

lowerRed = np.array([0,161,75])
upperRed = np.array([16,255,220])

lowerGreen = np.array([40,101,23])
upperGreen = np.array([59,250,158])

lowerYellow = np.array([16,106,114])
upperYellow = np.array([35,255,255])


while True:
	_, frame = camera.read()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	# print(frame.shape)
	cv.imshow("result", hsv)

	# CRIAÇÃO DE MASCARAS DE CORES
	maskBlue    = cv.inRange(hsv, lowerBlue, upperBlue)
	maskRed     = cv.inRange(hsv, lowerRed, upperRed)
	maskGreed   = cv.inRange(hsv, lowerGreen, upperGreen)
	maskYellow  = cv.inRange(hsv, lowerYellow, upperYellow)

	# CRIÇÃO DE BITWISE
	bitBlue     = cv.bitwise_and(frame, frame, mask=maskBlue)
	bitRed      = cv.bitwise_and(frame, frame, mask=maskRed)
	bitGreen    = cv.bitwise_and(frame, frame, mask=maskGreed)
	bitYellow   = cv.bitwise_and(frame, frame, mask=maskYellow)

	# GRAY OF ALL COLORS
	grayBlue 	= cv.cvtColor(bitBlue, cv.COLOR_BGR2GRAY)
	grayRed 	= cv.cvtColor(bitRed, cv.COLOR_BGR2GRAY)
	grayGreen 	= cv.cvtColor(bitGreen, cv.COLOR_BGR2GRAY)
	grayYellow	= cv.cvtColor(bitYellow, cv.COLOR_BGR2GRAY)

# MOVIMENTAÇÃO DO MOUSE COM A COR AZUL
#----------------------------------------------------
	_, borda = cv.threshold(grayBlue, 3, 255, cv.THRESH_BINARY)
	contornosBlue, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

	for contorno in contornosBlue:
		area = cv.contourArea(contorno)
		if area > 1200:
			(x, y, w, h) = cv.boundingRect(contorno)

			cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
			pyautogui.moveTo(1920-(x + w//2)*4, ((y + h//2)*1.6875))

# CLICK DO BOTÃO ESQUERDO COM A COR VERMELHA
#-----------------------------------------------------   
	_, borda = cv.threshold(grayRed, 3, 255, cv.THRESH_BINARY)
	contornosRed, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

	for contorno in contornosRed:
		area = cv.contourArea(contorno)
		if area > 1200 and coldown > 15:
			pyautogui.click(button="left")
			coldown = 0


# CLICK DO BOTÃO DIREITO COM A COR VERDE
#-----------------------------------------------------   
	_, borda = cv.threshold(grayGreen, 3, 255, cv.THRESH_BINARY)
	contornosGreen, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

	for contorno in contornosGreen:
		area = cv.contourArea(contorno)
		if area > 1200 and coldown > 15:
			pyautogui.click(button="right")
			coldown = 0


# FECHA O PROGRAMA COM A COR AMARELA
#-----------------------------------------------------   
	_, borda = cv.threshold(grayYellow, 3, 255, cv.THRESH_BINARY)
	contornosYellow, _ = cv.findContours(borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
	
	for contorno in contornosYellow:
		area = cv.contourArea(contorno)

		if area > 1200:
			break
			
	cv.imshow("Camera", frame)

	# FECHA O PROGRAMA COM TECLA DE ESC
	key = cv.waitKey(30)
	if key == 27:
		break

	if coldown <= 15:
		coldown += 1


cv.destroyAllWindows()
