import cv2

def main():
    cap = cv2.VideoCapture("data/PETS2009.webm")
    
    ret, frame1 = cap.read()
    height, width = frame1.shape[:2]

    codec = fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
    video = cv2.VideoWriter("output/frame_sub.mp4", codec, 30.0, (width, height),isColor=False)
    # https://plugout.hateblo.jp/entry/2020/01/10/085552

    

    while(cap.isOpened()):
        ret, frame2 = cap.read()
        if not ret:
            break

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # 背景差分
        mask = cv2.absdiff(gray2, gray1)

        video.write(mask)

        frame1 = frame2.copy()
    
    video.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()