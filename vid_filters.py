import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    check, img = video.read()
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    blur = cv2.blur(img, (5, 5))
    gblur = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    bilat = cv2.bilateralFilter(img, 9, 75, 75)

    cv2.imshow("orginal", img)
    cv2.imshow("2D Convolution", dst)
    cv2.imshow("blur", blur)
    cv2.imshow("GaussianBlur", gblur)
    cv2.imshow("Median", median)
    cv2.imshow("Bilateral", bilat)

    key = cv2.waitKey(1)
    if key == 27:
        break


video.release()
cv2.destroyAllWindows()
