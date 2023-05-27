#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

def ssd(arr1, arr2):
    assert len(arr1) == len(arr2)
    return sum((arr1 - arr2) ** 2)

def block_matching(im1, im2, window_size, shift, stride):

    # Initialize the matrices.
    w = int( (im2.shape[0] - window_size)//float(stride)+1)
    h = int( (im2.shape[1] - window_size)//float(stride)+1)

    px = np.zeros((w,h))
    py = np.zeros((w,h))
    vx = np.zeros((w,h))
    vy = np.zeros((w,h))
    colors =  np.zeros((w,h))
    wh = window_size // 2

    plot_plane = np.zeros(im2.shape)
    
    # Go through all the blocks.
    tx, ty = 0, 0

    # 格子位置に関するループ
    # （Windowの±whの範囲をstrideのステップ幅で走査する）
    for x in range(wh, im2.shape[0] - wh - 1, stride):
        for y in range(wh, im2.shape[1] - wh - 1, stride):
            nm = im2[x-wh:x+wh+1, y-wh:y+wh+1].flatten()
            
            min_dist = None
            flox, flowy = 0, 0
            curr_x, curr_y = 0, 0
            # テンプレートマッチング
            # SSDが最小になる位置を探索して位置の移動量を求める
            # 格子位置から±shiftの範囲で探索する
            for i in range(max(x - shift, wh), min(x + shift + 1, im1.shape[0] - wh - 1)):
                for j in range(max(y - shift, wh), min(y + shift + 1, im1.shape[1] - wh - 1)):
                    om = im1[i-wh:i+wh+1, j-wh:j+wh+1].flatten()
                    
                    # Compute the distance and update minimum.
                    dist = ssd(nm, om)
                    if not min_dist or dist < min_dist:
                        min_dist = dist
                        flowx, flowy = x - i, y - j
                        curr_x, curr_y = i, j
            
            # Update the flow field. 
            vx[-tx,ty] = flowy
            vy[-tx,ty] = flowx
            colors[-tx,ty] = np.sqrt(flowy**2+flowx**2)

            ty += 1
        tx += 1
        ty = 0
    
    return px, py, vx, vy, colors, plot_plane


#%%
prev_image = cv2.imread("./data/PET2009-fm1.bmp", 0)
curr_image = cv2.imread("./data/PET2009-fm2.bmp", 0)

px, py, vx, vy, colors, plot_plane = block_matching(prev_image, curr_image, window_size=10, shift=5, stride=5)

#%%
fig, ax = plt.subplots(figsize=(12,12))
ax.quiver(vx,vy,colors,cmap="jet")
ax.set_aspect("equal")
ax.axis("off")
#plt.imshow(plot_plane, cmap="gray")
#plt.show()