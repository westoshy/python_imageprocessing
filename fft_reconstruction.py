#%%
import cv2
import numpy as np

image = cv2.imread("data/Mandrill.bmp", 0)

image_fft = np.fft.fft2(image)
fshift = np.fft.fftshift(image_fft)


# 低周波数側から復元していく
for i in range(0,128,5):     

    conponents = np.zeros(image_fft.shape, dtype=image_fft.dtype)
    conponents[128-i:128+i, 128-i:128+i] = fshift[128-i:128+i, 128-i:128+i]
    ifshift = np.fft.ifftshift(conponents)

    image_ifft = np.fft.ifft2(ifshift).real.astype(np.uint8)

    magnitude_spectrum = 20 * np.log(np.abs(conponents))
    magnitude_spectrum = magnitude_spectrum.astype(np.uint8)

    cv2.imshow("reproducted", image_ifft)
    cv2.imshow("fft", magnitude_spectrum)
    cv2.waitKey(-1)

