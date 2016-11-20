import numpy as np
import cv2
def get_image():
     # read is the easiest way to get a full image out of a VideoCapture object.
     retval, im = cam.read()
     return im
cap = cv2.VideoCapture(0)
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
         break
camera_capture = get_image()
file = "test1.jpg"
 # A nice feature of the imwrite method is that it will automatically choose the
 # correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
cv2.destroyAllWindows()
