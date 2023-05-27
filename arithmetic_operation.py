import cv2

im1 = cv2.imread("data/Airplane.bmp", 0)
im2 = cv2.imread("data/Aerial.bmp", 0)

result = cv2.addWeighted(im1, 0.4, im2, 0.6, 0)

cv2.imshow("window", result)
cv2.waitKey(-1)
cv2.imwrite("add.bmp", result)