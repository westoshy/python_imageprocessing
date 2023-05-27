#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import time

template = cv2.imread("data/text_pattern.bmp")
image = cv2.imread("data/Text_flipped.bmp")

start = time.time()
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
mmr = cv2.minMaxLoc(result)

pos = mmr[3]

"""
x1 = result[pos[1]-1,pos[0]]
x2 = result[pos[1],pos[0]]
x3 = result[pos[1]+1,pos[0]]

# サブピクセル位置推定
d = (x3 - x1) / (x2 - x1)  * 0.5
print(d)
print(pos)
"""

#%%
dst = image.copy()
cv2.rectangle(dst, pos, (pos[0] + template.shape[1], pos[1] + template.shape[0]),
                     (0, 255, 0), 2)
print(time.time() - start)
"""
cv2.imshow("result", dst)
cv2.imwrite("output/matched.bmp", dst)
#cv2.imwrite("output/matched.bmp", result)
cv2.waitKey(-1)

plt.imshow(result, cmap="jet")
plt.show()

fig = plt.figure(figsize=(13, 10))
ax = fig.add_subplot(111, projection='3d')
# 格子点を生成
y, x = np.mgrid[:result.shape[0], :result.shape[1]]
color = ax.plot_surface(x, y, result, cmap='jet',
                        edgecolor='k', rstride=5, cstride=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(0, np.max(result.shape))
ax.set_ylim(0, np.max(result.shape))
cbar = plt.colorbar(color, shrink=0.6, label='z')
plt.show()
"""