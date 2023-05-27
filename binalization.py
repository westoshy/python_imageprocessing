import cv2
from matplotlib import pyplot as plt

image = cv2.imread("data/Text.bmp", 0)
threshold = 128
_, result1 = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
_, result2 = cv2.threshold(image, threshold, 255, cv2.THRESH_OTSU)

cv2.imshow("original", image)
cv2.imshow("processed(Fixed)", result1)
cv2.imshow("processed(Otsu)", result2)
cv2.imwrite("output/binalization_fixed.bmp", result1)
cv2.imwrite("output/binalization_otsu.bmp", result2)
cv2.waitKey(-1)
cv2.destroyAllWindows()

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist, color="black")
plt.xlim([0, 256])
plt.show()