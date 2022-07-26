from base64 import encode
import cv2
import numpy as np
# from cv2 import imshow
import face_recognition as fr
# import glob # for the file traversing
import os
from datetime import datetime

path = 'dataset'
images = []
classNames = []

myList = os.listdir(path)

print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])


        # Following conditional statement prevent the attendance of same person be entered again. Have to change this to accept entry within specified time periods.
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


        print(myDataList)



encodeListKnown = findEncodings(images)
print('Faces encoded ... ')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    facesCurFrame = fr.face_locations(imgS)
    encodeCurFrame = fr.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodeCurFrame, facesCurFrame):

        matches = fr.compare_faces(encodeListKnown, encodeFace)
        faceDis = fr.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)

        matchIndex = np.argmin(faceDis) 

        if matches[matchIndex]:
            if faceDis[matchIndex] < 0.50:
                name = classNames[matchIndex].upper()
                markAttendance(name)
            else:
                name = 'Unknown'
            # print(name)

            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1 * 4 ,x2*4 ,y2*4 ,x1 * 4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),3)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6, y2 - 6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
            # markAttendance(name)
        # cv2.rectangle(img,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(0,255,0),2)
        
        # cv2.rectangle(img,(x1,y1,x2,y2),(0,255,0),2)
       
    
    cv2.imshow('Attendance Management System',img)
    cv2.waitKey(1)
        
#########################################
# for cl in enumerate(myList):
#     for image in cl:
#         # currImg = cv2.imread(f'{pathlib}/{cl}/')
#         cLocation = f'{pathlib}/{cl}/{image}'
#         # print(cLocation)

#         currImg = cv2.imread(f'cLocation')

        
#         images.append(currImg)
#         Names.append(os.path.splitext(cl)[0])
#         # print(Names)
#         # print(images)
#         # cv2.imshow('img',currImg)

#########################################
