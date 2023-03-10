import cv2 as cv
#import numpy as np


face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0 , 0), 2)


    cv.imshow("Detection", frame)
    
    key = cv.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release
cv.destroyAllWindows()
