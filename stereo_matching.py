import numpy as np
import cv2
import matplotlib.pyplot as plt

mono0 = cv2.imread("data/stereo_L.png", 0)
mono1 = cv2.imread("data/stereo_R.png", 0)
stereo = cv2.StereoBM_create(blockSize= 15, numDisparities=64)
disparity = stereo.compute(mono0, mono1)
map = ( disparity - np.min(disparity) ) / ( np.max(disparity) - np.min(disparity) )
#blur = cv2.GaussianBlur(map, (15, 15), 5)


plt.style.use('default')
plt.imshow(disparity)
plt.axis("off")
plt.show()