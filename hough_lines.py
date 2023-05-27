import cv2
import numpy as np

img = cv2.imread('./data/Text.bmp')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_, edges = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)

lines = cv2.HoughLines(edges,3,np.pi/180,400)

print(lines)

for line in lines[:10]:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite("output/hough_edges.bmp", edges)
cv2.imwrite("output/hough_img.bmp", img)