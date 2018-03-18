import numpy as np
import cv2

def detect():
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')

    # open webcam
    cap = cv2.VideoCapture(0)

    while True:
        detected = False
        ret, frame = cap.read()
        # change to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # face detection
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            detected = True 

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & (0xff == ord('q')or detected) :
            break

    cap.release()
    cv2.destroyAllWindows()
    return frame
