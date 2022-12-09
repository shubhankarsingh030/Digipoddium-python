import cv2

camera = cv2.VideoCapture(0) # first webcamera
while camera.isOpened():
    status, image = camera.read()
    if not status:
        print("could not read image")
        break

    h,w,_ = image.shape
    image_bigger = cv2.resize(image,(2*w, 2*h))
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow("webcam window", image)
    cv2.imshow("bigger image", image_bigger)
    cv2.imshow("black and white image", image_bw)
    if cv2.waitKey(1) == 27: #27 means the ESC key
        break
camera.release()
cv2.destroyAllWindows()
