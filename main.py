import cv2
import random
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("E:/Project  Files/auto-selfie/haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("E:/Project  Files/auto-selfie/haarcascade_smile.xml")

while True:
    rt,video=cap.read()
    frame=video.copy()
    gray=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,1.2,6)
    for x,y,w,h in face:
        cv2.rectangle (video,(x,y),(x+w,y+h),(223,99,139),3)
        face_roi=video[y:y+h,x:x+w]   #roi=Region of interest
        gray_roi=gray[y:y+h,x:x+w]
        smile=smile_cascade.detectMultiScale(gray_roi,1.3,25)
        for x1,y1,w1,h1 in smile:
            cv2.rectangle (face_roi,(x1,y1),(x1+w1,y1+h1),(113,59,196),2)
            i=random.randint(1,100)
            file=f'Selfie{i}.png'
            cv2.imwrite(file,frame)
    cv2.imshow("Capture Selfie",video)
    if cv2.waitKey(1)==ord("q"):
        break