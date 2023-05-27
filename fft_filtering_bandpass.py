#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread("./data/Mandrill.bmp", 0)
f = np.fft.fft2(image)

# ローパス H(u,v)
mask = np.zeros(image.shape, dtype=np.uint8)
height, width = image.shape
cx = width // 2; cy = height // 2
cv2.circle(mask, center=(cx, cy), color=255, radius=60, thickness=-1)
cv2.circle(mask, center=(cx, cy), color=0, radius=30, thickness=-1)

# フィルタリング
filtered_shift = np.fft.fftshift(f) * mask
filtered = np.fft.ifftshift(filtered_shift)
img_ifft = np.fft.ifft2(filtered).real
output = cv2.normalize(img_ifft, None, 0, 255, cv2.NORM_MINMAX)

#%%
cv2.imshow("original", image)
magnitude = 20 * np.log(np.abs(np.fft.fftshift(f))) * mask / 255
cv2.imshow("band pass", magnitude.astype(np.uint8))
cv2.imshow("filtered", np.uint8(output))
cv2.waitKey(-1)


cv2.imwrite("output/band.bmp", magnitude.astype(np.uint8))
cv2.imwrite("output/filtered.bmp", np.uint8(output))


# %%
