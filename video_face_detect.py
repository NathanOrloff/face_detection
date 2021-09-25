import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')


capture = cv.VideoCapture(0) #reads video and stors in capture variable, integers go to live cameras or video path gets already saved video
#'Videos/EEDemo.mp4'
while True:
    isTrue, frame = capture.read() #reads each frame of the video, when reads frame returns frame and True

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=9)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), thickness=2)


    cv.imshow('Video', frame) #displays each frame
    if cv.waitKey(20) & 0xFF == ord('d'): #if the 'd' key is pressed break
        break

capture.release() #release video
cv.destroyAllWindows() 