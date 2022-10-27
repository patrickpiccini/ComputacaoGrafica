import cv2 as cv
import numpy as np

class Color():

    def __init__(self, frame) -> None:
        self.cam = frame

    def convert_to_gray(self):
        gray = cv.cvtColor(self.cam, cv.COLOR_BGR2GRAY)
        return gray
        
    def convert_to_hvs(self):
        hvs = cv.cvtColor(self.cam, cv.COLOR_BGR2HSV)
        return hvs

    def convert_to_lab(self):
        lab = cv.cvtColor(self.cam, cv.COLOR_BGR2LAB)
        return lab

