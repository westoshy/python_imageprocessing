import cv2
import numpy as np
import random as rand


image = cv2.imread("data/Cameraman.bmp" , 0) #グレースケール

height, width = image.shape
threshold = 128 
err = 0 

for i in range(height):
    for j in range(width):
        if image[i][j] + err < threshold:
            err = image[i][j] + err
            image[i][j] = 0
        else:
            err = image[i][j] + err - 255
            image[i][j] = 255

cv2.imshow("gray", image)
cv2.waitKey(-1)
cv2.imwrite("output/dithering.bmp", image)
cv2.destroyAllWindows()