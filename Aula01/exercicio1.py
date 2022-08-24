import cv2 as cv
import numpy as np

# image = cv.imread("images/venezuela.png")

image = cv.imread('../images/venezuela.png')

h, w, bpp = np.shape(image)
preto = np.array([0,0,0])
list_colors = []


for x in range(0,w):
    for y in range (0,h):
        color = [image[y,x][0],image[y,x][1],image[y,x][2]]
        if color not in list_colors:
            list_colors.append(color)

print(len(list_colors), 'cores')
