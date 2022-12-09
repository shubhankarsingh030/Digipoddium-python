import cv2

camera = cv2.VideoCapture(0) # first webcamera

while camera.isOpened():
    status, image = camera.read()
    if not status:
        print("could not read image")
        break
    #dp something with the image
    cv2.imshow("webcam window", image)
    if cv2.waitKey(1) == 27: #27 means the ESC key
        break
camera.release()
cv2.destroyAllWindows()
