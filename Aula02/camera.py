import cv2 as cv

# Open notebook camera
camera = cv.VideoCapture(0)


while True:
    _, frame = camera.read()
    cv.imshow("camera", frame)
    key = cv.waitKey(60)
    if key == 27:
        break
    if key == ord('s'):
        cv.imwrite('img.jpg', frame)

cv.waitKey(0)
cv.destroyAllWindows()