#%%
from matplotlib import pylab as plt
import numpy as np
import cv2

pix = 256                            #画像のサイズ
img = np.zeros((pix,pix)) #512行1列の2次元配列を512個、という3次元配列。画素値は8bit。カラー24bitにするときは1→3に。
out = np.zeros((pix,pix))
x = np.arange(pix)                   #0～511までのX軸を作成
y = np.arange(pix)   
[xx, yy] = np.meshgrid(x, y)
cycle1=15
cycle2=20
f = np.sin(2 * np.pi * (cycle1 * xx / pix + cycle2 * yy / pix))   #5周期分のサイン波を作成。振幅（画素値）は適当に。
#デバッグ用
#print(f.max())
#print(f.min())
#サイン波をimgに代入する
for i in range(pix):
    for j in range(pix):
        img[j][i] = f[j][i]

#デバッグ用
#plt.plot(x, f)
#plt.show()
#imgを画像として保存
cv2.normalize(img, out, 0, 255, cv2.NORM_MINMAX)
cv2.imwrite('gradation256.bmp', out)