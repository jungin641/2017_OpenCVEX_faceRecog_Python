import os
import numpy as np
import cv2
import Tkinter as tk
import Image, ImageTk
from PIL import Image

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

#for face detect
faceDetect=cv2.CascadeClassifier(r'C:\a_jungining\faceRecogPython\haarcascade_frontalface_default.xml');
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainningData.yml")

font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
#for training
path='dataSet'
sampleNum = 0
id = 0


def detect():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + h])
        if (id == 1):
            id = "Jungin"
        if (id == 2):
            id = "Yunmi"
        if (id == 3):
            id = "Jihoon"
        cv2.cv.PutText(cv2.cv.fromarray(frame), str(id), (x, y + h), font, 255);

    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, detect)


def dataSetCreate():
    print("dataSetCreateBtn pressed")
    global id
    id = raw_input('enter user id')
    dataSetCreateInLoop()


def dataSetCreateInLoop():
    global sampleNum
    global id
    _, frameforDSC = cap.read();
    frameforDSC = cv2.flip(frameforDSC, 1)
    grayforDSC = cv2.cvtColor(frameforDSC, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(grayforDSC, 1.3, 5);

    for (x, y, w, h) in faces:
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", grayforDSC[y:y + h, x:x + w])
        cv2.rectangle(frameforDSC, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100);
        sampleNum = sampleNum + 1;
        if (sampleNum > 20):
            break
    cv2image = cv2.cvtColor(frameforDSC, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    if (sampleNum < 20):
        lmain.after(10, dataSetCreateInLoop)
    else:
        sampleNum = 0



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



def training():
    Ids, faces = getIamgesWithID(path)
    rec.train(faces, Ids)
    rec.save('recognizer/trainningData.yml')
    cv2.destroyAllWindows()


#btn window (slider controls stage position)
btnFrame = tk.Frame(window, width=600, height=100)
btnFrame.grid(row = 600, column=0, padx=10, pady=2)

dataSetCreateBtn = tk.Button(btnFrame,
                    text="dataSetCreate", padx=10, pady=2, width=15,
                    command=dataSetCreate)
dataSetCreateBtn.pack(side=tk.LEFT)
trainingBtn = tk.Button(btnFrame,
                    text="Training", padx=10, pady=2, width=15,
                    command=training)
trainingBtn.pack(side=tk.LEFT)
detectBtn = tk.Button(btnFrame,
                    text="Detect", padx=10, pady=2, width=15)
detectBtn.pack(side=tk.LEFT)


detect()
window.mainloop()  # Starts GUI
