import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    scale_percent = 60  # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)

    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(frame, cv2.CV_64F, ksize=3)
    lap = np.uint8(np.absolute(lap))  # convert again in output format

    sobelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0)
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1)
    sobelY = np.uint8(np.absolute(sobelY))
    sobelComb = cv2.bitwise_or(sobelX, sobelY)

    canny = cv2.Canny(frame, 100, 200)

    cv2.imshow("SobelX", sobelX)
    cv2.imshow("SobelY", sobelY)
    cv2.imshow("SobelCombined", sobelComb)
    cv2.imshow("Laplacian", lap)
    cv2.imshow("Canny", canny)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
