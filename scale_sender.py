import socket
import time

# # Connect to fern server

# # Example: Send some changing values
# for scale in [0.5, 0.8, 1.0, 0.7, 0.9]:
    
#     time.sleep(3)

# sock.close()


import cv2
import mediapipe as mp
import numpy as np
import time
import handtrackingmodule as htm
import math

wcam , hcam =  1280,720

cap = cv2.VideoCapture(0) 
ptime = 0

detector = htm.handDetector(detectionCon=0.7)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5001))



while True:
    success , img = cap.read()
    img = detector.findHands(img, draw= False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) !=0:
        # print(lmList[4], lmList[8])
        x1 , y1 = lmList[4][1],lmList[4][2]
        x2 , y2 = lmList[8][1],lmList[8][2]

        cx, cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img , (x1,y1),2,(0,0,0),cv2.FILLED)
        cv2.circle(img , (x2,y2),2,(0,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(0,0,0),2)
        cv2.circle(img , (cx,cy),3,(0,0,0),cv2.FILLED,3)
        length = math.hypot(x2-x1 , y2-y1)
        # print(length)
        if length<30:
            cv2.circle(img , (cx,cy),3,(255,255,255),cv2.FILLED)

        min = 0.2
        max = 1
        # hand range = 50 - 200

        scale = np.interp(length,[50,300],[0.5, 1])
        print(scale)
        message = str(scale).encode()
        sock.sendall(message)
        print(f"[Sender] Sent scale {scale}")



    ctime = time.time()
    fps = 1/(ctime - ptime)
    ptime = ctime

    cv2.putText(img ,f"FPS:{int(fps)}",(40,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
    cv2.imshow("handvolume",img)

    cv2.waitKey(1)
