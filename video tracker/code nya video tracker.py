import cv2
filevideo= 'car video.mp4'
video = cv2.VideoCapture(filevideo)
database = 'cars.xml'
carTrack = cv2.CascadeClassifier(database)

while True:
    readStatus,frame= video.read()
    if readStatus:
        bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else: break
    car = carTrack.detectMultiScale(bw)
    for x,y,w,h in car:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,225,225),4)
    key = cv2.waitKey(1)
    if key ==32:
        break
    cv2.imshow("video Detector", frame)
cv2.destroyAllWindows()