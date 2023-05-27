import cv2
import numpy as np
from matplotlib import pyplot as plt

# めんどくさいのでグローバルに宣言
mouse_x = 0
mouse_y = 0
img_prev = cv2.imread("data/piv01_1.bmp") # 1つ前の時刻のの画像
img_curr = cv2.imread("data/piv01_2.bmp")
org_img = img_curr.copy()

# マウスコールバック（マウスポインタの位置をparamsに入れる）
def onMouse(event, x, y, flags, params):
    img_curr = org_img
    if event == cv2.EVENT_MOUSEMOVE:
        params["cx"] = x
        params["cy"] = y

# 位置x, yで作った窓が画像の外にはみ出さないことを確認する
def isValidRange(x, y, width, height, window_size):
    if (x - window_size > 0) and (y - window_size > 0) and (x + window_size < width) and (y + window_size < height):
        return True
    else:
        return False
#& (y + window_size < height)
def main():
    # callback function
    params = {"cx": -1, "cy": -1}
    cv2.namedWindow("corr map")
    cv2.namedWindow("t1 image")
    cv2.namedWindow("t2 image")
    cv2.namedWindow("search area")
    cv2.moveWindow("search area", 0, 0)
    cv2.moveWindow("corr map", 0, 120)
    cv2.moveWindow("t1 image", 150, 300)
    cv2.moveWindow("t2 image", 150, 0)
    cv2.setMouseCallback("t2 image", onMouse, params)

    search_size = 64
    block = 32
    height, width = img_curr.shape[:2]

    window = np.zeros([search_size, search_size,3], dtype=np.uint8)
    corr = np.zeros([search_size, search_size], dtype=np.uint8)
    template = np.zeros([block, block,3], dtype=np.uint8)

   

    while True:
        result = img_curr.copy()
        x = params["cx"]
        y = params["cy"]

        # 探索領域が画像からはみ出さないことをチェック
        if isValidRange(x, y, width, height, search_size//2):
            #correlation_function = cv2.TM_SQDIFF
            correlation_function = cv2.TM_CCORR
            window = img_curr[y-search_size//2:y+search_size//2, x-search_size//2:x+search_size//2]
            template = img_prev[ y-block//2:y+block//2, x-block//2:x+block//2]
            corr = cv2.matchTemplate(window, template, correlation_function)
            corr = np.uint8(cv2.normalize(corr, None, 0, 255, cv2.NORM_MINMAX))
            if correlation_function == cv2.TM_SQDIFF:
                corr = 255 - corr

        # マウスオーバーした位置に探索領域を描画する
        cv2.rectangle(result, 
                      (x-search_size//2,y-search_size//2), 
                      (x+search_size//2, y+search_size//2),
                      color=(0,255,00),thickness=1)        
        # 相関画像を疑似カラーに変換
        corr_result = cv2.applyColorMap(corr, cv2.COLORMAP_JET)

        cv2.imshow("t1 image", img_prev)
        cv2.imshow("t2 image", result)
        cv2.imshow("search area", window)
        cv2.imshow("corr map", corr_result)
        if cv2.waitKey(10) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()