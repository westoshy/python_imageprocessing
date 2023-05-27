import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("data/LAX_narrow.bmp", 0)
processed = cv2.normalize(image, np.zeros(image.shape), 0, 255, cv2.NORM_MINMAX)

hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_processed = cv2.calcHist([processed], [0], None, [256], [0, 256])
plt.plot(hist_image, color="gray")
plt.plot(hist_processed, color="black")
plt.xlim([0, 256])

cv2.imshow("orginal", image)
cv2.imshow("processed", processed)
plt.show()
cv2.waitKey(-1)