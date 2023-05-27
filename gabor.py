import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("data/Mandrill.bmp", 0)


gabor00 = cv2.getGaborKernel((30, 30), 4.0, np.radians(0), 10, 0.5, 0)
gabor45 = cv2.getGaborKernel((30, 30), 4.0, np.radians(45), 10, 0.5, 0)
gabor90 = cv2.getGaborKernel((30, 30), 4.0, np.radians(90), 10, 0.5, 0)
gabor135 = cv2.getGaborKernel((30, 30), 4.0, np.radians(135), 10, 0.5, 0)

dst00 = cv2.filter2D(img, -1, gabor00)
dst45 = cv2.filter2D(img, -1, gabor45)
dst90 = cv2.filter2D(img, -1, gabor90)
dst135 = cv2.filter2D(img, -1, gabor135)

fig = plt.figure()
ax1 = fig.add_subplot(2,4,1)
ax2 = fig.add_subplot(2,4,2)
ax3 = fig.add_subplot(2,4,3)
ax4 = fig.add_subplot(2,4,4)

ax5 = fig.add_subplot(2,4,5)
ax6 = fig.add_subplot(2,4,6)
ax7 = fig.add_subplot(2,4,7)
ax8 = fig.add_subplot(2,4,8)

ax1.imshow(gabor00, cmap="gray"); ax1.axis("off")
ax2.imshow(gabor45, cmap="gray"); ax2.axis("off")
ax3.imshow(gabor90, cmap="gray"); ax3.axis("off")
ax4.imshow(gabor135, cmap="gray"); ax4.axis("off")

ax5.imshow(dst00, cmap="gray"); ax5.axis("off")
ax6.imshow(dst45, cmap="gray"); ax6.axis("off")
ax7.imshow(dst90, cmap="gray"); ax7.axis("off")
ax8.imshow(dst135, cmap="gray"); ax8.axis("off")

plt.show()