import os
import cv2
import numpy as np
from ttk import *
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk

# creating global variable

global cam

# For dataSet Create
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
# For training
recognizer = cv2.createLBPHFaceRecognizer();
path = 'dataSet'
# For detect
rec = cv2.createLBPHFaceRecognizer();


class faceRecogApp:
    def __init__(self, master):

        frame = Frame(master, width=1000, height=700)
        frame.pack()

        circleCanvas = Canvas(frame, width=800, height=500, bg='pink')
        circleCanvas.grid(row=0, column=0, padx=10, pady=2)

        # initialize the root window and image panel

        btnFrame = Frame(frame, width=200, height=200)
        btnFrame.grid(row=1, column=0, padx=10, pady=2)

        self.dataSetCreateBtn = Button(btnFrame,
                                       text="dataSetCreate", fg="red", padx=10, pady=2, width=15,
                                       command=self.dataSetCreate)
        self.dataSetCreateBtn.pack(side=LEFT)
        self.trainingBtn = Button(btnFrame,
                                  text="Training", padx=10, pady=2, width=15,
                                  command=self.training)
        self.trainingBtn.pack(side=LEFT)
        self.detectBtn = Button(btnFrame,
                                text="Detect", padx=10, pady=2, width=15,
                                command=self.detect)
        self.detectBtn.pack(side=LEFT)
        self.detect()

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
        id = raw_input('enter user id')
        sampleNum = 0;
        while (True):
            ret, img = cam.read();
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
        cam.release()

    def training(self):
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
            ret, img = cam.read();
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


root = tk.Tk()
root.title("Face Detector by jungining");
app = faceRecogApp(root)
root.mainloop()
