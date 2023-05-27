import numpy as np
import cv2

image = cv2.imread("./data/text.bmp", 0)

# max/max filter using morphology calculation
kernel = np.ones((3,3), np.uint8)
min_image = cv2.erode(image, kernel)  # black region erosion is the same effect as min filter
max_image = cv2.dilate(image, kernel) # black region dilation is the same effect as max filter

# median filter
med_image = cv2.medianBlur(image, 3)

cv2.imshow("input image", image)
cv2.imshow("minimum filter", min_image)
cv2.imshow("maximum filter", max_image)
cv2.imshow("median filter", med_image)
cv2.waitKey(-1)

cv2.imwrite("output/min_image.bmp", min_image)
cv2.imwrite("output/max_image.bmp", max_image)
cv2.imwrite("output/med_image.bmp", med_image)