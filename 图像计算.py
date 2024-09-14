import cv2
import numpy as np

from matplotlib import pyplot as plt

img1=cv2.imread("../cat(1).jpg")
img2=cv2.imread("dog.jpg")
#img1+img2

img_dog=cv2.resize(img2,(500,414))
res=cv2.addWeighted(img1,0.4,img_dog,0.6,0)
plt.imshow(res)
plt.show()