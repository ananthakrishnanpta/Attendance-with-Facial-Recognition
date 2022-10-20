
## <font style="color:#aa0000">**Attendance-with-Facial-Recognition**</font>
<hr width="40%" align="left">
     An attendance system based on Facial recognition system. 
<hr width = "40%" align ="right">

### **The proposed system will have the following features :**
<hr>

1. Realtime face detection from camera
2. Face recognition
3. Updation of Employee attendance database along with time stamp of detection

---
---

### **Packages used in implementation**
- openCV and its haar xml files for face detection and further processing of frames
- face_recognition module to ease encodings of face data
- PyQt for interface to take Pictures

---
---

### **Approach**
    - Faces are detected and face locations recorded.
    - Encodings of detected faces for training are stored.
    - Faces detected from live camera feed.
    - Detected faces are encoded
    - encodings compared and matches detected.
    - On matches, employee name and timestamp are recorded and written into file.

Results:

    - Can identify employees and mark their attendance with less than a second's time.
    - Output successfully provides the timestamp of first appearance of face in the given runtime.


Limitations of using the proposed model:

    - Lack of high accuracy because of less number of training images given.
    - This model is based on comparison of single image encodings

---

Thank you ...

---
