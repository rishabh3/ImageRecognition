import cv2
from matplotlib import pyplot as plt
import numpy as np
file0=input("Enter the source file:")
file1=input("Enter the destination file:")
def edge(file0,file1):
    img = cv2.imread(file0,0)
    edges = cv2.Canny(img,120,120)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite(file1,edges)
edge(file0,file1)
