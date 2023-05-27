import numpy as np
import cv2

image = cv2.imread("data/Mandrill.bmp")

# 画像の高さと幅を取得
height, width = image.shape[:2]

zeros = np.zeros((height, width), image.dtype)
separated_img = cv2.split(image) 


img_B = cv2.merge((separated_img[0], zeros, zeros))
img_G = cv2.merge((zeros, separated_img[1], zeros))
img_R = cv2.merge((zeros, zeros, separated_img[2]))

cv2.imshow("Blue", img_B)
cv2.imshow("Green", img_G)
cv2.imshow("Red", img_R)
cv2.waitKey(-1)

cv2.imwrite("blue.bmp", img_B)
cv2.imwrite("Green.bmp", img_G)
cv2.imwrite("Red.bmp", img_R)