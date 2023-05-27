#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("./data/Sailboat.bmp", 0)
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
#fshift = f
magnitude_spectrum = 20 * np.log(np.abs(np.fft.fftshift(f)))
output = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
#cv2.imshow("spectrum", output.astype(np.uint8))
cv2.imshow("spectram_shifted.bmp", output.astype(np.uint8))
cv2.waitKey(-1)


#%%
#fig, ax = plt.subplots()
#ax.plot(output[128,:])
#ax.set_box_aspect(1)

#plt.imshow(magnitude_spectrum, cmap="gray")
#plt.show()

#%%
#cv2.imshow("fft", magnitude_spectrum)
#cv2.imwrite("fft.bmp", magnitude_spectrum)
#cv2.waitKey(-1)
