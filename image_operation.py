#%%
import numpy as np
import cv2
from matplotlib import pyplot as plt

"""
明るさとコントラストの変換
"""
def ajust(img, alpha, beta):
    lookUpTable = np.zeros((256,1), dtype="uint8")
    for x in range(256):
        y = alpha * x + beta
        lookUpTable[x][0] = y if y <= 255 else 255
    return lookUpTable

"""
ガンマ変換
"""
def gammaTransform(img, gamma):
    lookUpTable =np.zeros((256,1), dtype="uint8")
    for x in range(256):
        lookUpTable[x][0] = 255 * (x / 255) ** (1 / gamma)
    return lookUpTable


#%%

image = cv2.imread("data/couple.bmp", 0)
lookUpTable = ajust(image, alpha=2, beta=50)
result = cv2.LUT(image, lookUpTable)

#%%
image = cv2.imread("data/couple.bmp", 0)
lookUpTable = gammaTransform(image, gamma=2.0)
result = cv2.LUT(image, lookUpTable)

#%%
plt.plot(lookUpTable)
plt.xlim(0,255)
plt.ylim(0,256)

#%%
cv2.imshow("original", image)
cv2.imshow("processed", result)
cv2.imwrite("processed.bmp", result)
plt.show()
cv2.waitKey(-1)
