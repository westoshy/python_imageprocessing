import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("data/Mandrill.bmp", 0)

# エッジフィルタ
kernel = 1/9 * np.array(
    [[-1,-1,-1],
     [-1, 8,-1],
     [-1,-1,-1]]
)
edge_image = cv2.filter2D(image,-1,kernel)

# 3x3 ラプラシアンフィルタ
kernel = np.array(
    [[-1,-1,-1],
     [-1, 9,-1],
     [-1,-1,-1]]
)
unsharp_mask = cv2.filter2D(image,-1,kernel)

cv2.imwrite("output/edge.bmp", edge_image)
cv2.imwrite("output/unsharp_mask.bmp", unsharp_mask)