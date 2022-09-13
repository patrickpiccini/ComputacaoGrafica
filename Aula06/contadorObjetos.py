import cv2 as cv
import mahotas
camera = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:

    _, frame = camera.read()
    # etapas de processamento
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    suave = cv.blur(gray, (20, 20))
    #limiar = mahotas.thresholding.otsu(suave)
    # print(limiar)
    limiar = 112

    bordas = suave.copy()
    bordas[bordas > limiar] = 255
    bordas[bordas < 255] = 0
    bordas = cv.bitwise_not(bordas)

    objetos, _ = cv.findContours(
        bordas, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for item in objetos:
        area = cv.contourArea(item)
        if area > 400:
            (x, y, w, h) = cv.boundingRect(item)
            #cv.drawContours(frame, contorno, -1, (255,0,0), 2)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv.putText(frame, str(
                f"total: {len(objetos)}"), (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, 1)
            cv.putText(
                frame,
                str(f"x: {x} y: {y}"),
                (x, y-20),
                cv.FONT_HERSHEY_SIMPLEX,
                1, 1
            )

    print(len(objetos))

    #cv.imshow("Bordas", bordas)
    #cv.imshow("Suave", suave)
    #cv.imshow("Gray", gray)
    cv.imshow("Camera", frame)
    k = cv.waitKey(60)
    if k == 27:
        break

camera.release()
cv.destroyAllWindows()
