import cv2
import numpy as np
from matplotlib import pyplot as plt


def patternFilter(image, kernel):
    dst = cv2.filter2D(image,cv2.CV_16S,kernel)
    dst[dst < 0] = 0
    dst[dst > 255] = 255
    return dst


image = cv2.imread("data/kanji_text.bmp", 0)


#
# kernel pattern 1
#
kernel1 = np.array(
    [[-1,-1,-1],
     [ 1, 1, 1],
     [-1, -1,-1]]
)

dst1= patternFilter(image, kernel1)
cv2.imwrite("output/pattern_kernel1.bmp", dst1)

#
# kernel pattern 2
#
kernel2 = np.array(
    [[-1, 1,-1],
     [-1, 1,-1],
     [-1, 1,-1]]
)

dst2= patternFilter(image, kernel2)
cv2.imwrite("output/pattern_kernel2.bmp", dst2)

#
# kernel pattern 3
#
kernel3 = np.array(
    [[-1,-1, 1],
     [-1, 1,-1],
     [ 1,-1,-1]]
)

dst= patternFilter(image, kernel3)
cv2.imwrite("output/pattern_kernel3.bmp", dst)

#
# kernel pattern 4
#
kernel4 = np.array(
    [[ 1,-1,-1],
     [-1, 1,-1],
     [-1,-1, 1]]
)

dst= patternFilter(image, kernel4)
cv2.imwrite("output/pattern_kernel4.bmp", dst)

#
# kernel pattern 5
#
kernel5 = np.array(
    [[-1,-1,-1,-1,-1],
     [-1, 1, 1, 1,-1],
     [-1, 1, 1, 1,-1],
     [-1, 1, 1, 1,-1],
     [-1,-1,-1,-1,-1]]
)

dst= patternFilter(image, kernel5)
cv2.imwrite("output/pattern_kernel5.bmp", dst)

#
# kernel pattern 6
#
kernel6 = np.array(
    [[-1,-1,-1,-1,-1,-1,-1,-1],
     [ 1, 1, 1, 1, 1, 1, 1, 1],
     [-1,-1,-1,-1,-1,-1,-1,-1]]
)

dst= patternFilter(image, kernel6)
cv2.imwrite("output/pattern_kernel6.bmp", dst)