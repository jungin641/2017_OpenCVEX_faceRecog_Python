import cv2
import numpy as np


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")
id=5
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
while(True):
    ret,frame=cam.read();
    cv2image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(cv2image,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(cv2image[y:y+h,x:x+h])
        if(id==1) :
            id="Jungin"
        elif(id==2) :
            id="Yunmi"
        elif(id==3) :
            id="Mom"    
        cv2.cv.PutText(cv2.cv.fromarray(frame),str(id),(x,y+h),font,255);
    cv2.imshow("Face",frame);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
