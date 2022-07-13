import cv2
import numpy as np
import face_recognition
import os

path_List = []


def parseFiles():
    # function to parse through image dataset for model training
    pass


def face_detect():
    # function to detect, and return face array from image stream
    pass

def face_encode():
    # function to return face encodings for given image frame
    pass

def recognize():
    # function to return match for encoding for given detected face
    pass



#################################################################################################################################################################################
##                                                                               Test Code                                                                                     ##
#################################################################################################################################################################################


# brad_file  = "dataset/krishna/krishna1.jpg"
# brad_test = "dataset/krishna/krishna2.jpg"
brad_file = "dataset/brad/brad1.jpg"

brad_test = "dataset/brad/brad3.jpg"

imgBrad = face_recognition.load_image_file(brad_file)
imgBrad = cv2.cvtColor(imgBrad,cv2.COLOR_BGR2RGB)

img_test_brad = face_recognition.load_image_file(brad_test)
img_test_brad = cv2.cvtColor(img_test_brad,cv2.COLOR_BGR2RGB)


face_Loc = face_recognition.face_locations(imgBrad)[0]
encodeBrad = face_recognition.face_encodings(imgBrad)[0]
# print(encodeBrad)
cv2.rectangle(imgBrad,(face_Loc[3],face_Loc[0],face_Loc[1],face_Loc[2]),(255,0,0),2)


# for testing
face_Loc_test = face_recognition.face_locations(img_test_brad)[0]
encodeBrad_test = face_recognition.face_encodings(img_test_brad)[0]
cv2.rectangle(img_test_brad,(face_Loc_test[3],face_Loc_test[0],face_Loc_test[1],face_Loc_test[2]),(255,0,0),2)

# Comparison

results = face_recognition.compare_faces([encodeBrad],encodeBrad_test)

print(results)


cv2.imshow('Brad pitt',imgBrad)
cv2.imshow('Brad pitt test', img_test_brad)


cv2.waitKey(0)