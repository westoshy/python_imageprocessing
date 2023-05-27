import cv2
import numpy as np
import scipy.misc
from scipy.fftpack import dct, idct
import sys
from matplotlib import pyplot as plt

image = cv2.imread("data/Mandrill128.bmp", 0).astype(float)
image_F = dct(dct(image, axis=0), axis=1) ## 2D DCT of lenna

height, width = image.shape

index = 0
canvas = np.zeros((height,width))
output = np.zeros((height,width))
for h in range(height):
    for w in range(width):
        a = np.zeros((height,width))
        a[h,w] = 1
        base = idct(idct(a, axis=0), axis=1) ## create dct bases
        canvas += image_F[h,w] * base ## accumulate

        cv2.normalize(base, base, 0, 255, cv2.NORM_MINMAX)
        cv2.normalize(canvas, output, 0, 255, cv2.NORM_MINMAX)
        #scipy.misc.imsave("image-%03d-%03d.png" % (h, w), canvas)
        #cv2.imwrite("construct_dct/base-%03d-%03d.png" % (h, w), base.astype(np.uint8))
        cv2.imwrite("construct_dct_image/image-%05d.png" % index, output.astype(np.uint8))
        index = index + 1