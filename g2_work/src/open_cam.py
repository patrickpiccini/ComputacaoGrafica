import cv2 as cv
import numpy as np

from .convert_color import Color
# Open notebook camera    
class Camera():

    def __init__(self) -> None:
        self.camera = cv.VideoCapture(0, cv.CAP_DSHOW)
                

    def open_camera(self) -> None:
        while True:
            _, frame = self.camera.read()

            self.color = Color(frame)
            gray = self.color.convert_to_gray()
            cv.imshow("camera1", gray)

            hvs = self.color.convert_to_hvs()
            cv.imshow("camera2", hvs)

            lab = self.color.convert_to_lab()
            cv.imshow("camera3", lab)
            key = cv.waitKey(60)
            if key == 27:
                break


        cv.waitKey(0)
        cv.destroyAllWindows()