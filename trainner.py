import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet'

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

Ids,faces=getIamgesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()
