import cv2,datetime
face_cascade=cv2.CascadeClassifier("package/haarcascade_eye.xml")
face_cascade1=cv2.CascadeClassifier("package/haarcascade_frontalface_default.xml")

font=cv2.FONT_HERSHEY_COMPLEX
video=cv2.VideoCapture(0)

while True:
    check,gray=video.read()

    #gray=cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,
                                    scaleFactor=1.05,
                                    minNeighbors=5)

    for x,y,w,h in faces:
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),3)
        gray=cv2.putText(gray,"EYES",(x,y),font,.2,(0,255,0))


    faces=face_cascade1.detectMultiScale(gray,
                                        scaleFactor=1.05,
                                        minNeighbors=5)

    for x,y,w,h in faces:
        gray=cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)
        gray=cv2.putText(gray,"FACE",(x,y),font,.5,(0,255,0))

    datetim=str(datetime.datetime.now())
    gray=cv2.putText(gray,datetim,(10,10),font,.5,(0,255,0))


    #time.sleep(3)
    cv2.imshow("photo",gray)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
