import cv2

face_cascade1 = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
face_cascade2 = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")


def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


font = cv2.FONT_HERSHEY_COMPLEX
video = cv2.VideoCapture(0)
while True:
    check, gray1 = video.read()
    gray = rescaleFrame(gray1)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    faces = face_cascade1.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    faces2 = face_cascade2.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        x = x * 2
        y = y * 2
        w = w * 2
        h = h * 2
        gray1 = cv2.rectangle(gray1, (x, y), (x + w, y + h), (255, 0, 0), 3)  # BGR -->BLue
        gray1 = cv2.putText(gray1, "FACE", (x, y), font, 0.5, (0, 0, 255))  # BGR -->Red
    faces = face_cascade1.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces2:
        x = x * 2
        y = y * 2
        w = w * 2
        h = h * 2
        gray1 = cv2.rectangle(gray1, (x, y), (x + w, y + h), (255, 255, 0), 3)  # BGR -->BLue
        gray1 = cv2.putText(gray1, "EYE", (x, y), font, 0.5, (0, 255, 255))  # BGR -->Red
    cv2.imshow("photo", gray1)
    key = cv2.waitKey(100)
    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
