
#%%
import cv2
import numpy as np
import statistics
from matplotlib import pyplot as plt


image = cv2.imread("data/airplane.bmp")

# ヒストグラムの表示
color = ("b", "g", "r")
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

# 各色成分の基本統計量の算出
separated_img = cv2.split(image) 
print("最大値 B:", np.max(separated_img[0]), 
      "G:", np.max(separated_img[1]), 
      "R:", np.max(separated_img[2]))
print("最小値 B:", np.min(separated_img[0]), 
      "G:", np.min(separated_img[1]), 
      "R:", np.min(separated_img[2]))
print("平均値 B:", np.mean(separated_img[0]), 
      "G:", np.mean(separated_img[1]), 
      "R:", np.mean(separated_img[2]))
print("第一四分位数 B:", np.percentile(separated_img[0], 25), 
      "G:", np.percentile(separated_img[1], 25), 
      "R:", np.percentile(separated_img[2], 25))
print("中央値 B:", np.median(separated_img[0]), 
      "G:", np.median(separated_img[1]), 
      "R:", np.median(separated_img[2]))
print("第三四分位数 B:", np.percentile(separated_img[0], 75), 
      "G:", np.percentile(separated_img[1], 75), 
      "R:", np.percentile(separated_img[2], 75))
print("最頻値 B:", statistics.mode(separated_img[0].flatten().tolist()), 
      "G:", statistics.mode(separated_img[1].flatten().tolist()), 
      "R:", statistics.mode(separated_img[2].flatten().tolist()))
print("分散 B:", np.var(separated_img[0]), 
      "G:", np.var(separated_img[1]), 
      "R:", np.var(separated_img[2]))
