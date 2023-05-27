# Standard imports
import cv2
import numpy as np
 
# Read image
im = cv2.imread("data/figures.bmp", 1)
 
### ------- パラメータの初期化
params = cv2.SimpleBlobDetector_Params() 

# ブロブ領域（minArea <= blob < maxArea）
params.filterByArea = True
params.minArea = 100

# 真円度（ 4∗π∗Area / perimeter∗perimeter によって定義される）
#（minCircularity <= blob < maxCircularity）
params.filterByCircularity = True 
params.minCircularity = 0.90

# 凸面の情報（minConvexity <= blob < maxConvexity）
params.filterByConvexity = True
params.minConvexity = 0.1

# 楕円形を表す（minInertiaRatio <= blob < maxInertiaRatio）
params.filterByInertia = False
params.minInertiaRatio = 0.1

### ------- パラメータの初期化

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

cv2.imwrite("output/detect_blob.bmp", im_with_keypoints)