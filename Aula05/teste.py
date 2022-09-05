import cv2 as cv
import numpy as np
import pyautogui
camera = cv.VideoCapture(0, cv.CAP_DSHOW)
sizeScreen = pyautogui.size()
count = 0
cd = 10

#   y   x
#   4, 1,6875
x = y = w = h = 1
while 1:
    _, frame = camera.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # print(frame.shape)
    cv.imshow("result", hsv)

    lowerBlue = np.array([96, 142, 75])
    upperBlue = np.array([255, 255, 255])

    lowerRed = np.array([0, 151, 78])
    upperRed = np.array([255, 255, 255])

    lowerOrange = np.array([0, 140, 134])
    upperOrange = np.array([255, 255, 255])

    maskBlue    = cv.inRange(hsv, lowerBlue, upperBlue)
    maskRed     = cv.inRange(hsv, lowerRed, upperRed)
    maskOrange  = cv.inRange(hsv, lowerOrange, upperOrange)

    bitBlue     = cv.bitwise_and(frame, frame, mask=maskBlue)
    bitRed      = cv.bitwise_and(frame, frame, mask=maskRed)
    bitOrange   = cv.bitwise_and(frame, frame, mask=maskOrange)

#----------------------------------------------------
    gray = cv.cvtColor(bitBlue, cv.COLOR_BGR2GRAY)


    

    #cv.imshow("result mask", borda)
    cv.imshow("result", maskBlue)


    k = cv.waitKey(60)
    if k == 27:
        break

camera.release()
cv.destroyAllWindows()
