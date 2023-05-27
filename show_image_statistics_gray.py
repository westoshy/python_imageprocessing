
#%%
import cv2
import numpy as np
import statistics
from matplotlib import pyplot as plt


image = cv2.imread("data/Mandrill.bmp", 0)

# ヒストグラムの表示
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist, color="gray")
plt.xlim([0, 256])
plt.show()

# 各色成分の基本統計量の算出
print("最大値:", np.max(image))
print("最小値:", np.min(image))
print("平均値:", np.mean(image))
print("第一四分位数:", np.percentile(image, 25))
print("中央値:", np.median(image))
print("第三四分位数:", np.percentile(image, 75))
print("最頻値:", statistics.mode(image.flatten().tolist()))
print("分散:", np.var(image[0]))
