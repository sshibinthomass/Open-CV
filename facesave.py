import cv2, os

for count, filename in enumerate(os.listdir("my_pics/")):
    img = cv2.imread("my_pics/photo" + str(count) + ".jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.5, minNeighbors=5)

    for x, y, w, h in faces:
        crop = img[y : y + h, x : x + w]
        crop = cv2.resize(crop, (254, 254))
        # cv2.imshow('Image', crop)
        cv2.imwrite("face/face" + str(count) + ".jpg", crop)
