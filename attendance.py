import cv2
from cv2 import imshow
import face_recognition as fr
import glob # for the file traversing
import os
pathlib = 'dataset'
images = []
Names = []
image_Dict = {}
myList = os.listdir(pathlib)
print(myList)
for cl in myList:
    currImg = cv2.imread(f'{pathlib}/{cl}/')
    images = [cv2.imread(file) for file in glob.glob(f'{pathlib}/{cl}/*.jpg')]
    # print(f'{pathlib}/{cl}')
    images.append(currImg)
    Names.append(os.path.splitext(cl)[0])
    print(Names)
    print(images)
    image_Dict[Names] = images

print(image_Dict)
    # cv2.imshow('img',currImg)

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
