import cv2
import face_recognition
import os
path = 'dataset'
images = []
classNames = []

myList = os.listdir(path)
print()