import numpy as np

w,h=np.meshgrid(range(0, img.shape[1], 10), range(0, img.shape[0], 10))
pts = (np.vstack((w.flatten(), h.flatten())).T).astype('float32')
pts_new = cv2.undistortPoints(np.array([pts]), camera_mat, dist_coef, P=camera_mat)[0]

plt.scatter(pts[:,0], pts[:,1], 20, 'r', alpha=.5)
plt.scatter(pts_new[:,0], pts_new[:,1], 20, 'b', alpha=