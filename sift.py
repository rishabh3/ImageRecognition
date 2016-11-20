import cv2
import numpy as np
file1=input("Enter the file:")
file2=input("Enter the destination file:")
img = cv2.imread(file1)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
dummy=np.zeros((1,1))
img=cv2.drawKeypoints(gray,kp,dummy,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite(file2,img)
