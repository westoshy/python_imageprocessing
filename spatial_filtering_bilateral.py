import cv2

img = cv2.imread("data/Parrots_128.bmp", 0)

dst1 = cv2.GaussianBlur(img, (3,3), 3)
# バイラテラルフィルタ
dst2 = cv2.bilateralFilter(img, 3, sigmaColor=50, sigmaSpace=20)
cv2.imshow("gaussian filter", dst1)
cv2.imshow("bilateral filter", dst2)
cv2.waitKey(-1)

cv2.imwrite("output/gaussian.bmp", dst1)
cv2.imwrite("output/bilateral.bmp", dst2)