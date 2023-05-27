import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("data/Mandrill.bmp", 0)

# 3x3 平均値フィルタ
#kernel = np.ones((3,3),np.float32)/9
kernel = 1/9 * np.array(
    [[1,1,1],
     [1,1,1],
     [1,1,1]]
)
dst_mean3x3 = cv2.filter2D(image,-1,kernel)

# 5x5 平均値フィルタ
kernel = np.ones((5,5),np.float32)/25
kernel = 1/25 * np.array(
    [[1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1],
     [1,1,1,1,1]]
)
dst_mean5x5 = cv2.filter2D(image,-1,kernel)

# 3x3 ガウシアンフィルタ
kernel = 1/16 * np.array(
    [[1,2,1],
     [2,4,2],
     [1,2,1]]
)
dst_gaussian3x3 = cv2.filter2D(image,-1,kernel)

# 5x5 ガウシアンフィルタ
kernel = np.ones((5,5),np.float32)/25
kernel = 1/256 * np.array(
    [[1,  4,  6,  4, 1],
     [4, 16, 24, 16, 4],
     [6, 24, 36, 24, 6],
     [4, 16, 24, 16, 4],
     [1,  4,  6,  4, 1]]
)
dst_gaussian5x5 = cv2.filter2D(image,-1,kernel)

cv2.imshow("original", image)

cv2.imshow("mean 3x3", dst_mean3x3)
cv2.imshow("mean 5x5", dst_mean5x5)

cv2.imshow("gaussian 3x3", dst_gaussian3x3)
cv2.imshow("gaussian 5x5", dst_gaussian5x5)

cv2.imwrite("output/mean_3x3.bmp", dst_mean3x3)
cv2.imwrite("output/mean_5x5.bmp", dst_mean5x5)
cv2.imwrite("output/gaussian_3x3.bmp", dst_gaussian3x3)
cv2.imwrite("output/gaussian_5x5.bmp", dst_gaussian5x5)

cv2.waitKey(-1)