import numpy as np
from matplotlib import pyplot as plt
import cv2

# Select distortion pattern
distortion0 = np.array([+0.0, 0.000, 0.0, 0.0, 0.00]) # no distortion
distortion = np.array([-0.3, 0.001, 0.0, 0.0, 0.01])
#distortion = np.array([+0.3, 0.001, 0.0, 0.0, 0.01])

# Generate Grid of Object Points
grid_size, square_size = [20, 20], 0.2
object_points = np.zeros([grid_size[0] * grid_size[1], 3])
mx, my = [(grid_size[0] - 1) * square_size / 2, (grid_size[1] - 1) * square_size / 2]
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        object_points[i * grid_size[0] + j] = [i * square_size - mx, j * square_size - my, 0]

# Setup the camera information
f, p = [5e-3, 120e-8]
intrinsic = np.array([[f/p, 0, 0], [0, f/p, 0], [0, 0, 1]])
rvec = np.array([0.0, 0.0, 0.0])
tvec = np.array([0.0, 0.0, 3.0])


# Project the points
image_points0, jacobian0 = cv2.projectPoints(object_points, rvec, tvec, intrinsic, distortion0)
image_points, jacobian = cv2.projectPoints(object_points, rvec, tvec, intrinsic, distortion)

# Plot the points (using PyPlot)
plt.scatter(*zip(*image_points0[:, 0, :]), marker='.')
plt.scatter(*zip(*image_points[:, 0, :]), marker='.')
plt.axis('equal')
plt.xlim((-4000, 4000))
plt.ylim((-4000, 4000))
#plt.grid()
plt.axis("off")
plt.show()