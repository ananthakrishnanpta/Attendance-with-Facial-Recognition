from time import time
import cv2  
import time as tt
  
# Load the cascade  
face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_alt.xml')  
  
# To capture video from webcam.   
cap = cv2.VideoCapture(0)  


img_name = ('detected_images/'+str(x) +'.png' for x in range(0,1000))
while True:  
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  

        # looping through
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
        
        
        crop_img = img[y:y+h, x:x+w]
        tt.sleep(0.5)
        cv2.imwrite(str(next(img_name)),crop_img)
        
    # Display  
    cv2.imshow('Video', img)

  
    # Stop if escape key is pressed  
    k = cv2.waitKey(30) & 0xff  
    
    if k==27:  
        break  
          
# Release the VideoCapture object  
cap.release()