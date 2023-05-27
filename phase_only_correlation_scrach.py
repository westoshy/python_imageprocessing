import numpy as np
import cv2
from scipy.optimize import leastsq
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def pocfunc_model(alpha, delta1, delta2, r, u):
    N1, N2 = r.shape
    V1, V2 = list(map(lambda x: 2 * x + 1, u))
    return lambda n1, n2: alpha / (N1 * N2) * np.sin((n1 + delta1) * V1 / N1 * np.pi) * np.sin((n2 + delta2) * V2 / N2 * np.pi)\
                                            / (np.sin((n1 + delta1) * np.pi / N1) * np.sin((n2 + delta2) * np.pi / N2))
img_g1 = cv2.imread('data/Mandrill_pos1.bmp', 0).astype(np.float32)
img_g2 = cv2.imread('data/Mandrill_pos2.bmp', 0).astype(np.float32)

# opencv implementetion
(x, y), e = cv2.phaseCorrelate(img_g1, img_g2)
print(e, 'Y=' + str(y), 'x=' + str(x))

# scrach implementation
img_f1 = np.fft.fft2(img_g1)
img_f2 = np.fft.fft2(img_g2).conjugate()
img_f = img_f1 * img_f2
img_n = img_f / np.abs(img_f)
img_p = np.fft.ifft2(img_n).real
img_p = np.fft.fftshift(img_p)
m = np.floor(list(map(lambda x: x / 2.0, img_g1.shape)))
u = list(map(lambda x: x / 2.0, m))
max_pos = np.argmax(img_p)
peak = (int(max_pos / img_g1.shape[1]), max_pos % img_g1.shape[1])
max_peak = img_p[peak[0], peak[1]]
fitting_shape = (9, 9)
mf = np.floor(list(map(lambda x: x / 2.0, (fitting_shape))))
fitting_area = img_p[int(peak[0] - mf[0]) : int(peak[0] + mf[0] + 1), int(peak[1] - mf[1]) : int(peak[1] + mf[1] + 1)]

p0 = [0.5, -(peak[0] - m[0]) - 0.02, -(peak[1] - m[1]) - 0.02]
y, x = np.mgrid[-mf[0]:mf[0] + 1, -mf[1]:mf[1] + 1]
y = y + peak[0] - m[0]
x = x + peak[1] - m[1]
errorfunction = lambda p: np.ravel(pocfunc_model(p[0], p[1], p[2], img_p, u)(y, x) - fitting_area)
plsq = leastsq(errorfunction, p0)

#plt.imshow(img_p)
#plt.show()

fig = plt.figure(figsize=(13, 10))
ax = fig.add_subplot(111, projection='3d')
# 格子点を生成
y, x = np.mgrid[:img_p.shape[0], :img_p.shape[1]]
color = ax.plot_surface(x, y, img_p, cmap='jet',
                        edgecolor='k', rstride=5, cstride=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xlim(0, np.max(img_p.shape))
ax.set_ylim(0, np.max(img_p.shape))
cbar = plt.colorbar(color, shrink=0.6, label='z')
plt.show()


print(plsq[0][0], 'Y=' + str(plsq[0][1]), 'x=' + str(plsq[0][2]))