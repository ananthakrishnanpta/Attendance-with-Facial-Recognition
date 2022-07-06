import cv2
import numpy as np
import face_recognition
import os

path_List = []


def parseFiles():
    pass


def face_detect():
    pass

def face_encode():
    pass

#################################################################################################################################################################################
##                                                                               Test Code                                                                                     ##
#################################################################################################################################################################################



brad_file = "dataset/brad/brad1.jpg"

brad_test = "dataset/brad/brad2.jpg"

imgBrad = face_recognition.load_image_file(brad_file)
imgBrad = cv2.cvtColor(imgBrad,cv2.COLOR_BGR2RGB)

img_test_brad = face_recognition.load_image_file(brad_test)
img_test_brad = cv2.cvtColor(img_test_brad,cv2.COLOR_BGR2RGB)


face_Loc = face_recognition.face_locations(imgBrad)[0]
encodeBrad = face_recognition.face_encodings(imgBrad)[0]
print(encodeBrad)





cv2.imshow('Brad pitt',imgBrad)
cv2.imshow('Brad pitt test', img_test_brad)


cv2.waitKey(0)