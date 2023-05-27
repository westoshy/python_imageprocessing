import cv2

image = cv2.imread("data/Mandrill.bmp")
cv2.imshow("Window", image)
cv2.waitKey(-1)