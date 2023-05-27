import cv2
import numpy as np

# Load images
sample1=cv2.imread("data/Mandrill_pos1.bmp", 0) 
sample2=cv2.imread("data/Mandrill_pos2.bmp", 0)

# calculate phase only correlation
(x_shift, y_shift), response = cv2.phaseCorrelate(sample1.astype(np.float32), sample2.astype(np.float32))

# print x-shift, y-shift and response
print(x_shift, " pixel", y_shift, "pixel")
print(type(response))