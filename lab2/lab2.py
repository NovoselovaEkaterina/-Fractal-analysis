# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WQR8w7c_l8Nz3G5z-rrYfFC4Hyl9ffoy
"""



import cv2
from google.colab.patches import cv2_imshow
import PIL
from PIL import Image
i= Image.open('43.jpg')
h, w = i.size

originalImage = cv2.imread('43.jpg')
img=originalImage
cv2_imshow(img)

#cv2_imshow(originalImage)
#img = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
#cv2_imshow(img[:,:,2])

for i in range(w):
  for j in range(h):
    img[i][j][0]=0
    img[i][j][1]=0
    
cv2_imshow(img)