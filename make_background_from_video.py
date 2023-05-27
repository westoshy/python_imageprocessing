import cv2
import numpy as np

cap = cv2.VideoCapture("data/PETS2009.webm")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
background_image = np.zeros((height, width))

i = 0
while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        background_image = background_image + gray / length
    else:
        break
result = np.uint8(background_image)

cv2.imshow("background", result)
cv2.waitKey(-1)
cv2.imwrite("output/background.bmp", result)
cv2.destroyWindow("background")