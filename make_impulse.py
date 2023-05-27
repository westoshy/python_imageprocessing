from matplotlib import pylab as plt
import numpy as np
import cv2
pix = 256                          #画像のサイズ
img = np.zeros((pix,pix,1),np.uint8) #512行1列の2次元配列を512個、という3次元配列。画素値は8bit。カラー24bitにするときは1→3に。

cycle = 16
for i in range(pix):
    for j in range(pix):

        if i % cycle == 0 and j % cycle == 0:
            img[j][i] = 255
#デバッグ用
#plt.plot(x, f)
#plt.show()
#imgを画像として保存
cv2.imwrite('inpulse16.bmp', img)