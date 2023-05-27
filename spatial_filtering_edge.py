import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("data/Mandrill.bmp", 0)

# 3x3 ラプラシアンフィルタ
kernel = np.array(
    [[-1,-1,-1],
     [-1, 8,-1],
     [-1,-1,-1]]
)
dst_laplacian3x3 = cv2.filter2D(image,-1,kernel)

# 5x5 平均値フィルタ
kernel = 1/25 * np.array(
    [[-1, -3, -4, -3, -1],
     [-3,  0,  6,  0, -3],
     [-4,  6, 20,  6, -4],
     [-3,  0,  6,  0, -3],
     [-1, -3, -4, -3, -1]]
)
dst_laplacian5x5 = cv2.filter2D(image,-1,kernel)

# 3x3 Sobel縦フィルタ
kernel = np.array(
    [[-1,-2,-1],
     [ 0, 0, 0],
     [ 1, 2, 1]]
)
dst_sobel_vertial = cv2.filter2D(image,-1,kernel)

# 5x5 ガウシアンフィルタ
kernel = np.ones((5,5),np.float32)/25
kernel = np.array(
    [[-1, 0, 1],
     [-2, 0, 2],
     [-1, 0, 1]]
)
dst_sobel_horizontal = cv2.filter2D(image,-1,kernel)

cv2.imshow("original", image)

cv2.imshow("laplacian 3x3", dst_laplacian3x3)
cv2.imshow("laplacian 5x5", dst_laplacian5x5)

cv2.imshow("sobel(vertical)", dst_sobel_vertial)
cv2.imshow("sobel(horizontal)", dst_sobel_horizontal)

cv2.imwrite("output/mean_3x3.bmp", dst_laplacian3x3)
cv2.imwrite("output/mean_5x5.bmp", dst_laplacian5x5)
cv2.imwrite("output/sobel_vertical.bmp", dst_sobel_vertial)
cv2.imwrite("output/sobel_horizontal.bmp", dst_sobel_horizontal)

cv2.waitKey(-1)