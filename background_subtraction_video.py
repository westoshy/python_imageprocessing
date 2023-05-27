import cv2

def main():
    cap = cv2.VideoCapture("data/PETS2009.webm")
    ret, frame = cap.read()
    height, width = frame.shape[:2]

    background = cv2.imread("data/background.bmp", 0)

    codec = fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
    video = cv2.VideoWriter("output/background_sub1.mp4", codec, 30.0, (width, height),isColor=False)
    # https://plugout.hateblo.jp/entry/2020/01/10/085552

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 背景差分
        mask = cv2.absdiff(gray, background)

        video.write(gray)

        #cv2.imshow("mask", mask)
        #cv2.imshow("gray", gray)        

        #if cv2.waitKey(39) & 0xFF == ord("q"):
        #    break
    
    video.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()