import cv2

#load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontface_default.xml')
test = face_cascade.load('haarcascade_frontalface_default.xml')
print(test)

#to capture video from webcam
cap = cv2.VideoCapture(0)

while (True):
    # read the frame
    _, img = cap.read()
    # convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # draw the ractangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0), 2)
        # display
        cv2.imshow('img', img)
        # stop if escape is pressed

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

#release the videocapture object
cap.release()
cv2.destroyAllWindow()