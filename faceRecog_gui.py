import os
import cv2
import numpy as np
from ttk import *
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk

#creating global variable
global last_frame                                      
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)
global cam


# For dataSet Create
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
# For training
recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet'
# For detect
rec=cv2.createLBPHFaceRecognizer();

class App:
 def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.show_vid()
    self.dataSetCreateBtn = Button(frame, 
                         text="dataSetCreate", fg="red",width=25,height=3,
                         command=self.dataSetCreate)
    self.dataSetCreateBtn.pack(side=LEFT)
    self.trainingBtn = Button(frame,
                         text="Training",width=25,height=3,
                         command=self.training)
    self.trainingBtn.pack(side=LEFT)
    self.detectBtn = Button(frame,
                         text="Detect",width=25,height=3,
                         command=self.detect)
    self.detectBtn.pack(side=LEFT)
 def show_vid():                                        #creating a function
    if not cap.isOpened():                             #checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if flag is None:
        print "Major error!"
    elif flag:
        global last_frame
        last_frame = frame.copy()

    pic = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)
 def getIamgesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces
 def dataSetCreate(self):
    print("dataSetCreateBtn pressed")
    id=raw_input('enter user id')
    sampleNum=0;
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            sampleNum=sampleNum+1;
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(100);
        #cv2.imshow("Face",img);
        cv2.waitKey(1);
        if(sampleNum>20):
            break
    cam.release()
 def training(self):
    print("trainingBtn pressed")
    Ids,faces=getIamgesWithID(path)
    recognizer.train(faces,Ids)
    recognizer.save('recognizer/trainningData.yml')
   
 def detect(self):
    print("detectBtn pressed")
    recognizer.load("recognizer\\trainningData.yml")
    id=0
    font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    while(True):
        ret,img=cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=recognizer.predict(gray[y:y+h,x:x+h])
            if(id==1) :
                id="Jungin"
            if(id==2) :
                id="Yunmi"
            if(id==3) :
                id="Mom"    
            cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
        if(cv2.waitKey(1)==ord('q')):
            break;
root = Tk()
lmain = tk.Label(master=root)
lmain.grid(column=0, rowspan=4, padx=5, pady=5)
root.title("Face Detector by jungining");
app = App(root)
root.mainloop()
