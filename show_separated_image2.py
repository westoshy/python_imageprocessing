import numpy as np
import cv2

image = cv2.imread("data/Mandrill.bmp")

# 画像の高さと幅を取得
height, width = image.shape[:2]

separated_img = cv2.split(image) 
cv2.imwrite("output/separated_b.bmp", separated_img[0])
cv2.imwrite("output/separated_g.bmp", separated_img[1])
cv2.imwrite("output/separated_r.bmp", separated_img[2])

# CIE XYZ color space
xyz_image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
separated_img = cv2.split(xyz_image) 
cv2.imwrite("output/separated_x.bmp", separated_img[0])
cv2.imwrite("output/separated_y.bmp", separated_img[1])
cv2.imwrite("output/separated_z.bmp", separated_img[2])

# CIE L*a*b* color space
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
separated_img = cv2.split(lab_image) 
cv2.imwrite("output/separated_L-star.bmp", separated_img[0])
cv2.imwrite("output/separated_a-star.bmp", separated_img[1])
cv2.imwrite("output/separated_b-star.bmp", separated_img[2])

# YCbCr color space
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
separated_img = cv2.split(ycbcr_image) 
cv2.imwrite("output/separated_Y.bmp", separated_img[0])
cv2.imwrite("output/separated_Cb.bmp", separated_img[1])
cv2.imwrite("output/separated_Cr.bmp", separated_img[2])

# HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
separated_img = cv2.split(hsv_image) 
cv2.imwrite("output/separated_H.bmp", separated_img[0])
cv2.imwrite("output/separated_S.bmp", separated_img[1])
cv2.imwrite("output/separated_V.bmp", separated_img[2])