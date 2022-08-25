# pip install pyzbar
import cv2 as cv
from pyzbar.pyzbar import decode

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    frame = camera.read()[1]
    dados = decode(frame)
    
    for dado in dados:
        (x,y,w,h) = dado.rect
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)


    cv.imshow("Camera", frame)

    k = cv.waitKey(60)
    if k==27:
        break

camera.release()
cv.destroyAllWindows()