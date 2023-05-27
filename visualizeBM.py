#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt

def ssd(arr1, arr2):
    assert len(arr1) == len(arr2)
    return sum((arr1 - arr2) ** 2)

def block_matching(im1, im2, window_size, block_size, stride):

    # Initialize the matrices.
    w = int( (im2.shape[0] - window_size)//float(stride)+1)
    h = int( (im2.shape[1] - window_size)//float(stride)+1)

    px = np.zeros((w,h))
    py = np.zeros((w,h))
    vx = np.zeros((w,h))
    vy = np.zeros((w,h))
    colors =  np.zeros((w,h))
    wh = window_size // 2
    shift = block_size // 2
    
    # Go through all the blocks.
    tx, ty = 0, 0
    idx = 0

    # 格子位置に関するループ
    # （Windowの±whの範囲をstrideのステップ幅で走査する）
    for y in range(wh, im2.shape[1] - wh - 1, stride):
        for x in range(wh, im2.shape[0] - wh - 1, stride):

            

            # テンプレートマッチング
            # SSDが最小になる位置を探索して位置の移動量を求める
            # 格子位置から±shiftの範囲で探索する
            sy = max(y - shift, wh)
            fy = min(y + shift + 1, im1.shape[1] - wh - 1)
            sx = max(x - shift, wh)
            fx = min(x + shift + 1, im1.shape[0] - wh - 1)

            cx = (sx + fx) // 2
            cy = (sy + fy) // 2

            for j in range(sy, fy):
                for i in range(sx, fx):
                    height, width = im2.shape
                    plot_plane = np.zeros((height, width, 3))
                    plot_plane[cy, cx] = (0,0,255)
                    cv2.rectangle(plot_plane,(sx-wh,sy-wh), (fx+wh-1, fy+wh), color=(0,255,0))
                    cv2.rectangle(plot_plane,(i-wh,j-wh), (i+wh-1, j+wh), color=(0,255,0))

                    cv2.imwrite("blockmatching/scan_%05d.bmp" % idx, plot_plane)
                    idx = idx + 1
                    #cv2.waitKey(-1)

    return px, py, vx, vy, colors, plot_plane


#%%
prev_image = cv2.imread("./data/PET2009-fm1_32.bmp", 0)
curr_image = cv2.imread("./data/PET2009-fm2_32.bmp", 0)

#
# stride: ブロック走査の間隔
# shift: ブロックの大きさ
px, py, vx, vy, colors, plot_plane = block_matching(prev_image, curr_image, window_size=10, block_size=15, stride=5)

#%%
#fig, ax = plt.subplots(figsize=(12,12))
#ax.quiver(vx,vy,colors,cmap="jet")
#ax.set_aspect("equal")
#ax.axis("off")
plt.imshow(plot_plane, cmap="gray")
plt.show()