import cv2

face_cascade_db = cv2.CascadeClassifier("MyLib/faces.xml")

img = cv2.imread("3.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade_db.detectMultiScale(img, 1.1, 19)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),
                  (x+w,y+h), (0,0,255),2)

cv2.imshow('result', img)
cv2.waitKey()