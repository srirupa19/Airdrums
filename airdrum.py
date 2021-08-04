import numpy as np
# just write import cv2
import cv2
from pygame import mixer
import winsound

cap = cv2.VideoCapture(0)
detector = cv2.SimpleBlobDetector_create()

    
while True:

    _,frame = cap.read()

    hsv=cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.rectangle(frame,(100,100),(250,250),(255,0,0),3)
    cv2.rectangle(frame,(50,300),(200,400),(200,0,100),3)
    cv2.rectangle(frame,(400,300),(600,400),(100,50,300),3)

    kernel = np.ones((5,5),np.uint8)

    dst = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours , _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    blob = max(contours, key=lambda el: cv2.contourArea(el))
    M = cv2.moments(blob)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
    cv2.circle(frame, center, 5, (0,0,255), -1)
    if (center[0]>100 and center[0]<250 )and(center[1]>100 and center[1]<250):
        cv2.circle(frame, center, 8, (0,255,0), 2)
       
        winsound.PlaySound("H.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        winsound.Beep(600,000)
        mixer.init()
        mixer.music.load("H.wav")
        mixer.music.play()
    elif (center[0]>50 and center[0]<200 )and(center[1]>300 and center[1]<400):
        cv2.circle(frame, center, 8, (0,255,0), 2)
        winsound.PlaySound("C.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        winsound.Beep(600,000)
        mixer.init()
        mixer.music.load("C.wav")
        mixer.music.play()
    elif (center[0]>400 and center[0]<600 )and(center[1]>300 and center[1]<400):
        cv2.circle(frame, center, 8, (0,255,0), 2)
        winsound.PlaySound("T.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
        winsound.Beep(600,000)
        mixer.init()
        mixer.music.load("T.wav")
        mixer.music.play()
    

    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
