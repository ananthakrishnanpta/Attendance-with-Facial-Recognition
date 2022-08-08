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
empName = []

paths_list = os.listdir(path)

print(paths_list)

for person in paths_list:
    imgFrame = cv2.imread(f'{path}/{person}')
    images.append(imgFrame)
    empName.append(os.path.splitext(person)[0])

# print(empName)

def findEncodings(images):
    faces_encode_list = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        encode = fr.face_encodings(img)[0]
        faces_encode_list.append(encode)

    return faces_encode_list


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
            print(f"{name} signed in at {dtString}")


        # print(myDataList)



encodeListKnown = findEncodings(images)
print('Faces encoded ... ')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    capturedSource = cv2.resize(img,(0,0),None,0.25,0.25)
    capturedSource = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    facesCurFrame = fr.face_locations(capturedSource)
    encodeCurFrame = fr.face_encodings(capturedSource,facesCurFrame)

    for encodeFace,faceLoc in zip(encodeCurFrame, facesCurFrame):

        matches = fr.compare_faces(encodeListKnown, encodeFace)
        face_distances = fr.face_distance(encodeListKnown, encodeFace)
        # print(face_distances)

        indicesMatch = np.argmin(face_distances) 

        if matches[indicesMatch]:
            if face_distances[indicesMatch] < 0.50:
                name = empName[indicesMatch].upper()
                markAttendance(name)
            else:
                name = 'Unknown'
            # print(name)

            top,right,bottom,left = faceLoc
            top,right,bottom,left = top * 4 ,right*4 ,bottom*4 ,left * 4
            # cv2.rectangle(img,(left,top),(right,bottom),(255,0,0),3)
            # cv2.rectangle(img,(left,bottom-35),(right,bottom),(0,255,0),cv2.FILLED)
            # cv2.putText(img,name,(left+6, bottom - 6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            # ##
            cv2.rectangle(img, (top, right), (left + top, right + bottom), (0, 255, 0), 2)
            cv2.putText(img, name, (top, right), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
            # markAttendance(name)
        # cv2.rectangle(img,(faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(0,255,0),2)
        
        # cv2.rectangle(img,(left,top,right,bottom),(0,255,0),2)
       
    
    cv2.imshow('Attendance Management System',img)
    cv2.waitKey(1)
        
#########################################
# for person in enumerate(paths_list):
#     for image in person:
#         # currImg = cv2.imread(f'{pathlib}/{person}/')
#         cLocation = f'{pathlib}/{person}/{image}'
#         # print(cLocation)

#         currImg = cv2.imread(f'cLocation')

        
#         images.append(currImg)
#         Names.append(os.path.splitext(person)[0])
#         # print(Names)
#         # print(images)
#         # cv2.imshow('img',currImg)

#########################################
