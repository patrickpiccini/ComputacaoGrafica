import cv2 as cv
import numpy as np
from datetime import datetime

dateNow = datetime.now()
dateFormate = dateNow.strftime('%d%m%Y%H%M%S')

image = cv.imread('../images/simpsons.jpg')
height, width, bpp = np.shape(image)

resizeImage = cv.resize(image, (int(width/3), int(height/3) ) ,interpolation=cv.INTER_CUBIC )
cv.imwrite(f"{dateFormate}.png", resizeImage)

cv.waitKey(0)
cv.destroyAllWindows()