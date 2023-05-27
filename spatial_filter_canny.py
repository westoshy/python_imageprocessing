import cv2
import numpy as np

img = cv2.imread('data/Girl.bmp',0)
edges1 = cv2.Canny(img, 10, 50)
edges2 = cv2.Canny(img, 10, 100)
edges3 = cv2.Canny(img, 10, 150)

cv2.imshow("edge1", edges1)
cv2.imshow("edge2", edges2)
cv2.imshow("edge3", edges3)
cv2.waitKey(-1)

cv2.imwrite("output/canny_edge1.bmp", edges1)
cv2.imwrite("output/canny_edge2.bmp", edges2)
cv2.imwrite("output/canny_edge3.bmp", edges3)