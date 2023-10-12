import enum
import cv2
import numpy as np
import os
import crud
import face_recognition
from database import SessionLocal, engine
import schema

schema.Base.metadata.create_all(bind=engine)


# Dependency

db = SessionLocal()
path = 'Image_recog/'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []


    for i,img in enumerate(images):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        print("encode:: ",encode)
        crud.create_user(db,encode,classNames[i])
        encodeList.append(encode)
        
    return encodeList

if __name__ == "__main__":
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
