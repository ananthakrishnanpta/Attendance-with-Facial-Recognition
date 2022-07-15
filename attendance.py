import cv2
from cv2 import imshow
import face_recognition as fr

import os
pathlib = 'dataset'
images = []
Names = []
myList = os.listdir(pathlib)
print(myList)
for cl in myList:
    currImg = cv2.imread(f'{pathlib}/{cl}')
    images.append(currImg)
    Names.append(os.path.splitext(cl)[0])
    #print(Names)
    # print(images)
