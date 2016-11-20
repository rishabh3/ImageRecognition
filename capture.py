import cv2
from matplotlib import pyplot as plt
import numpy as np
a=input("Enter the file where you want to store:")
b=input("Enter the final destination image:")
cam = cv2.VideoCapture(0)
ramp_frames=30
def get_image():
     # read is the easiest way to get a full image out of a VideoCapture object.
     retval, im = cam.read()
     return im
for i in range(ramp_frames):
     temp = get_image()
print("Taking image...")
     # Take the actual image we want to keep
camera_capture = get_image()
 # A nice feature of the imwrite method is that it will automatically choose the
 # correct format based on the file extension you provide. Convenient!
cv2.imwrite(a, camera_capture)

 # You'll want to release the camera, otherwise you won't be able to create a new
 # capture object until your script exits
del(cam)
# def plot():
#      file1="test_blur.jpg"
#      img=cv2.imread('test.jpg')
#      blur=cv2.blur(img,(1,1))
#      cv2.imwrite(file1, blur)
# plot()
def edges(n,m):
      gray=cv2.imread(n,0)
      img=cv2.imread(n)
      mask = np.zeros(img.shape[:2],np.uint8)
      bgdModel = np.zeros((1,65),np.float64)
      fgdModel = np.zeros((1,65),np.float64)
      rect = (75,75,450,290)
      cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
      mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
      img1 = img*mask2[:,:,np.newaxis]
      #print(img1)
      bc=img-img1

      bc[np.where((bc > [0,0,0]).all(axis = 2))] = [0,0,0]
      final = bc + img1
      print(final)
      cv2.imshow('image', final )
      k = cv2.waitKey(0)
      if k==27:
        cv2.destroyAllWindows()
      #plt.imshow(img),plt.colorbar(),plt.show()
      cv2.imwrite(m,final)
edges(a,b)
# def edge():
#     img = cv2.imread('test.jpg',0)
#     edges = cv2.Canny(img,130,200)
#     plt.subplot(121),plt.imshow(img,cmap = 'gray')
#     plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#     plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#     plt.show()
# edge()
# filename = 'test.png'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# #result is dilated for marking the corners, not important
# dst = cv2.dilate(dst,None)
#
# # Threshold for an optimal value, it may vary depending on the image.
# img[dst>0.01*dst.max()]=[0,0,255]
#
# cv2.imshow('dst',img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
# img = cv2.imread('test.png')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# corners = np.int0(corners)
#
# for i in corners:
#     x,y = i.ravel()
#     cv2.circle(img,(x,y),3,255,-1)
#
# plt.imshow(img),plt.show()
