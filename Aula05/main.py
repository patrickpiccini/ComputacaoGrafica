import cv2 as cv
import numpy as np
import pyautogui
import numpy as np

TEMPO_LEITURA = 30

#Ponto menor para a cor Azul
lowerBlue = np.array([85,123,120])
#Ponto maior para a cor Azul
upperBlue = np.array([153,205,191])

#Ponto menor para a cor Vermelha
lowerOrange = np.array([0,121,212])
#Ponto maior para a cor Vermelha
upperOrange = np.array([42,208,255])

#Ponto menor para a cor Laranja
lowerRed = np.array([153,99,102])
#Ponto maior para a cor Laranja
upperRed = np.array([205,198,255])

#Captura de altura e largura do monitor onde o codigo está rodando
alturaMonitor, larguraMonitor = pyautogui.size()

#Seleção da primeira camera que o dispositivo esta rodando
camera = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    #Leitura da imagem da camera, pegando o segundo valor que retorna da funcao
    frame = camera.read()[1]

    #Flipar o frame, para que o movimento da cor para esquerda e direita não fique invertido
    frame = cv.flip(frame, 1)
    
    #Redimensionamento da camera para o tamanho do monitor
    #Para que o mouse consiga ser movimentado por toda a tela
    frame = cv.resize(frame, (alturaMonitor, larguraMonitor), interpolation=cv.INTER_CUBIC)   

    #Conversao da imagem de BGR para HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Faz mascara na imagem da camera, baseado nos limites do Azul
    maskBlue = cv.inRange(hsv, lowerBlue, upperBlue)
    #Aplica a mascara no frame, para manter a cor
    bitBlue = cv.bitwise_and(frame, frame, mask=maskBlue)
    #Conversao do frame mascarado para tons de cinza
    grayBlue = cv.cvtColor(bitBlue, cv.COLOR_BGR2GRAY)
    #Acentua as bordas
    borderBlue = cv.threshold(grayBlue, 3, 255, cv.THRESH_BINARY)[1]
    #Identifica as bordas
    contornosBlue = cv.findContours(borderBlue, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
    
    #Faz mascara na imagem da camera, baseado nos limites do Vermelho
    maskRed = cv.inRange(hsv, lowerRed, upperRed)
    bitRed = cv.bitwise_and(frame, frame, mask=maskRed)
    grayRed = cv.cvtColor(bitRed, cv.COLOR_BGR2GRAY)
    borderRed = cv.threshold(grayRed, 3, 255, cv.THRESH_BINARY)[1]
    contornosRed = cv.findContours(borderRed, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]

    #Faz mascara na imagem da camera, baseado nos limites do Laranja
    maskOrange = cv.inRange(hsv, lowerOrange, upperOrange)
    bitOrange = cv.bitwise_and(frame, frame, mask=maskOrange)
    grayOrange = cv.cvtColor(bitOrange, cv.COLOR_BGR2GRAY)
    borderOrange = cv.threshold(grayOrange, 3, 255, cv.THRESH_BINARY)[1]
    contornosOrange = cv.findContours(borderOrange, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[0]
    
    #Passar por todos os contornos identificados para o Azul
    for contorno in contornosBlue:
        #Calcular a area do contorno atual
        area = cv.contourArea(contorno)

        #Se esse contorno tiver uma area maior de 800 px²
        if area > 1200:
            #Identifica a posição que fica o primeiro pixel do contorno
            (x,y,w,h) = cv.boundingRect(contorno)

            #Calculo para saber o ponto central da area do contorno
            x = (x + x+w) //2
            y = (y + y+h) // 2

            #Move o mouse para a posicao identificada
            pyautogui.moveTo(x, y)    

    for contorno in contornosRed:
        area = cv.contourArea(contorno)

        if area > 800:
            #Clicara o botão esquerdo do mouse
            pyautogui.click(button="left")    

    for contorno in contornosOrange:
        area = cv.contourArea(contorno)

        if area > 800:
            #Clicara o botão direito do mouse
            pyautogui.click(button="right")

    #Mostra o frame capturado da camera
    cv.imshow('coisa', frame)

    #Faz uma leitura das teclas pressionadas de 60 em 60 milisecs
    key = cv.waitKey(TEMPO_LEITURA)

    #Se a tecla pressionada for o 'Esc', para o loop
    if key == 27:
        break

#Forca a destruicao de todas as janelas abertas pelo algoritmo
cv.destroyAllWindows()