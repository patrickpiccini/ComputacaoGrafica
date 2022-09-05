import cv2 as cv
import numpy as np
camera = cv.VideoCapture(0, cv.CAP_DSHOW)


while 1:
    _, frame = camera.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowerBlue = np.array([102, 74, 112])
    upperBlue = np.array([255, 255, 255])

    mask = cv.inRange(hsv, lowerBlue, upperBlue)
    result = cv.bitwise_and(frame, frame, mask=mask)

    gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    _, borda = cv.threshold(gray, 3, 255, cv.THRESH_BINARY)

    contornos, _ = cv.findContours(
        borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv.contourArea(contorno)
        if area > 800:
            (x, y, w, h) = cv.boundingRect(contorno)
            #cv.drawContours(frame, contorno, -1, (255,0,0), 2)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv.putText(
                frame,
                str(f"x: {x} y: {y}"),
                (x, y-20),
                cv.FONT_HERSHEY_SIMPLEX,
                1, 1
            )

    #cv.imshow("result mask", borda)
    cv.imshow("result", frame)
    k = cv.waitKey(60)
    if k == 27:
        break

camera.release()
cv.destroyAllWindows()
