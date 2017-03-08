import os
import numpy as np
import cv2
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500,bg='red')
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

recognizer = cv2.createLBPHFaceRecognizer();
path = 'dataSet'

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def getIamgesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L');
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces

def dataSetCreate(self):
    print("dataSetCreateBtn pressed")
    # For dataSet Create
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    id = raw_input('enter user id')
    sampleNum = 0;
    while (True):
        ret, img = cap.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1;
            cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.waitKey(100);
        # cv2.imshow("Face",img);
        cv2.waitKey(1);
        if (sampleNum > 40):
            break
        cap.release()

def training(self):
    # For training

    print("trainingBtn pressed")
    Ids, faces = self.getIamgesWithID(path)
    recognizer.train(faces, Ids)
    recognizer.save('recognizer/trainningData.yml')

def detect(self):
    print("detectBtn pressed")
    recognizer.load("recognizer\\trainningData.yml")
    id = 0
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
    while (True):
        ret, img = cap.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = recognizer.predict(gray[y:y + h, x:x + h])
            if (id == 1):
                id = "Jungin"
            if (id == 2):
                id = "Yunmi"
            if (id == 3):
                id = "Mom"
            cv2.cv.PutText(cv2.cv.fromarray(img), str(id), (x, y + h), font, 255);
        if (cv2.waitKey(1) == ord('q')):
            break;


#btn window
btnFrame = tk.Frame(window, width=600, height=100)
btnFrame.grid(row = 600, column=0, padx=10, pady=2)

dataSetCreateBtn = tk.Button(btnFrame,
                             text="dataSetCreate", fg="red", padx=10, pady=2, width=15,
                             command=dataSetCreate)
dataSetCreateBtn.pack(side=tk.LEFT)
trainingBtn = tk.Button(btnFrame,
                           text="Training", padx=10, pady=2, width=15,
                           command=training)
trainingBtn.pack(side=tk.LEFT)
detectBtn = tk.Button(btnFrame,
                           text="Detect", padx=10, pady=2, width=15,
                           command=detect)
detectBtn.pack(side=tk.LEFT)

show_frame()  #Display 2
window.mainloop()  #Starts GUI
