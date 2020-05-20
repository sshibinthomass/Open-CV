import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output1.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame", frame)

        out.write(frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
