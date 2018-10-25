# coding=utf-8
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
video = cv2.VideoCapture(0)
edges = None
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale = 1
fontColor = (255, 255, 0)
lineType = 2
while 1:
    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print(len(eyes))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            roi_eye_gray = gray[ey:ey + eh, ex:ex + ew]
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.putText(img, '%s faces found' % (len(faces)),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)
    cv2.imshow('img', img)
video.release()
cv2.destroyAllWindows()
