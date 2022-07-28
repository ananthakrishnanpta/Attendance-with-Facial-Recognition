# <font style="color:red">Attendance-with-Facial-Recognition</font>
## An attendance system based on Facial recognition system. 
<hr>

### The proposed system will have the following features : 
<hr>

1. Realtime face detection from camera
2. Face recognition
3. Updation of Employee attendance database along with time stamp of detection

---
---

### Packages used in implementation
- openCV and its haar xml files for face detection and further processing of frames
- face_recognition module to ease encodings of face data
- PyQt for interface to take Pictures

---
---

### 
                    ### Results:

                    - Can identify employees and mark their attendance with less than a second's time.
                    - Output successfully provides the timestamp of first appearance of face in the given runtime.


                    ### Limitations of using the proposed model:

                    - Lack of high accuracy because of less number of training images given.
                    - This model is based on comparison of single image encoding and the distance comparison of encoding of detected face and hence depends on a single set of encodings. Other face features are not taken into consideration to increase response time in limited system resources.


