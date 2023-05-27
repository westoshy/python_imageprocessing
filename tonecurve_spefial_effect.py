import numpy as np
import cv2

img = cv2.imread("data/Mandrill.bmp", 0)

# ネガポジ変換
x = np.arange(256)
y = 255 - x
dst = cv2.LUT(img, y)
cv2.imwrite("output/negpos.bmp", dst)

# ポスタリゼーション
x = np.arange(256)
steps = 4
bins = np.linspace(0, 255, steps + 1)
y = np.array([bins[i - 1] for i in np.digitize(x, bins)]).astype(int)
dst = cv2.LUT(img, y)
cv2.imwrite("output/posterization.bmp", dst)

# ソラリゼーション
x = np.arange(256)
y = (np.sin(x * 2 * np.pi / 255) + 1) * 255 / 2
dst = cv2.LUT(img, y)
cv2.imwrite("output/solarization.bmp", dst)

# 疑似カラー
dst = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imwrite("output/pseudo.bmp", dst)


