import cv2

background = cv2.imread("data/background.bmp")
source = cv2.imread("data/frame.bmp")

result = cv2.absdiff(background, source)
cv2.imshow("subtract", result)
cv2.imwrite("output/subtraction.bmp", result)
cv2.waitKey(-1)