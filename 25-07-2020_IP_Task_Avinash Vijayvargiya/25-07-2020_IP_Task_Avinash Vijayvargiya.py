import cv2 # importing opencv library

# READING FILES
face_cascade = cv2.CascadeClassifier(r'C:\Users\DELL\Desktop\Day 3\Session 3\haarcascade_frontalface_default.xml') # loading files
eye_cascade = cv2.CascadeClassifier(r'C:\Users\DELL\Desktop\Day 3\Session 3\haarcascade_eye.xml')

# VIDEO ACCESSING
cap = cv2.VideoCapture(0)

oldX, oldY = 0, 0

# INFINITE LOOP
while True:
    # storing image frames into image object 'image'
    ret, image = cap.read(0)
    # converting to gray scale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 'detectMultiscale' command operated on 'face_cascade'
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    # FACE DETECTION
    for (x, y, w, h) in faces:
      # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 200), 2)
        cv2.line(image, (x, y), (x + 30, y), (0, 255, 200), 2)
        cv2.line(image, (x, y), (x, y + 30), (0, 255, 200), 2)
        cv2.line(image, (x+w, y+h), (x+w - 30, y+h), (0, 255, 200), 2)
        cv2.line(image, (x+w, y+h), (x+w, y+h - 30), (0, 255, 200), 2)
        cv2.line(image, (x+w, y), (x+w - 30, y), (0, 255, 200), 2)
        cv2.line(image, (x+w, y), (x+w, y + 30), (0, 255, 200), 2)
        cv2.line(image, (x, y+h), (x + 30, y+h), (0, 255, 200), 2)
        cv2.line(image, (x, y+h), (x, y+h - 30), (0, 255, 200), 2)
        # CONDITIONS FOR DIRECTION
        if ( oldX > x + 3 ):
            # print("Left")
            dir = 'Left Motion Detected'
        elif ( oldX < x - 3 ):
            # print("Right")
            dir = 'Right Motion Detected'
        else:
            # print("Same")
            dir = 'No Motion Detected'
        oldX, oldY = x, y
        # DIRECTION RESULT PRINTING
        cv2.putText(image, "Motion :" + dir, (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1)  # printing result of direction

    # DISPLAY OUTPUT
    resImage = cv2.resize(image, (600, 600))
    cv2.imshow("Direction", resImage)

    # EXIT CONTROL
    k = cv2.waitKey(1)
    if (k == ord('q')):
        break

# OTHER EXIT CONTROLS
cap.release()
cv2.destroyAllWindows()
