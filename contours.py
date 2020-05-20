import cv2
import numpy as np


video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    scale_percent = 60 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    frame=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours (thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)


    cv2.imshow("Contours", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


video.release()
cv2.destroyAllWindows()
