import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("data/Girl.bmp", 0)
result = cv2.equalizeHist(image)
cv2.imshow("original", image)
cv2.imshow("processed", result)
cv2.waitKey(-1)
cv2.imwrite("output/histogram_equalized.png", result)

hist_org = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_processed = cv2.calcHist([result], [0], None, [256], [0, 256])
plt.plot(hist_org, color="gray")
plt.plot(hist_processed, color="black")
plt.xlim([0, 256])
plt.show()
