import cv2
from matplotlib import pyplot as plt
import numpy as np

file_path=input("Enter the file name ending with jpg: ")
file1=input("Enter the file name ending with jpg: ")
def edges(file0,file1):
      gray=cv2.imread(file1,0)
      img=cv2.imread(file1)
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
      cv2.imwrite(file0,final)
edges(file_path,file1)
