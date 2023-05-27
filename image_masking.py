import cv2
import numpy as np


image = cv2.imread("data/Mandrill.bmp", 0)

mask = np.zeros(image.shape, np.uint8)
cv2.rectangle(mask, pt1=(50,100), pt2=(150, 200), color=255, thickness=-1)
masked = cv2.bitwise_and(image, mask)

cv2.imshow("mask", mask)
cv2.imshow("masked", masked)

cv2.imwrite("mask.bmp", mask)
cv2.imwrite("masked.bmp", masked)

cv2.waitKey(-1)