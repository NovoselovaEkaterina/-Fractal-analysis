# -*- coding: utf-8 -*-
"""flab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pTboMkvvGPj6g5taBb96XVenUgVMFKAE
"""

import numpy as np
import matplotlib.pyplot as plt 
import cv2
from google.colab.patches import cv2_imshow

originalImage = cv2.imread('001.PNG')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
#blackAndWhiteImage.resize(b,b)
#cv2_imshow(originalImage)
cv2_imshow(grayImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

def ublanket(img):
  k,l=img.shape
  u=np.ndarray(img.shape)
  for i in range(k-1):
    for j in range(l-1):
      u[i][j]=max(img[i][j]+1,img[i-1][j],img[i][j-1],img[i+1][j],img[i][j+1])          
  return u

def bblanket(img):
  k,l=img.shape
  b=np.ndarray(img.shape)
  for i in range(k-1):
    for j in range(l-1):
      b[i][j]=min(img[i][j]-1,img[i-1][j],img[i][j-1],img[i+1][j],img[i][j+1])
  return b

def getVol(u,b):
  k,l=u.shape
  vol=0.0
  for i in range(k):
    for j in range(l):
      vol=vol+u[i][j]-b[i][j]

  return vol

def getA(img):
  u1=ublanket(img)
  u2=ublanket(u1)
  b1=bblanket(img)
  b2=bblanket(b1)
  vol1=getVol(u1,b1)
  vol2=getVol(u2,b2)
  A1=(vol2-vol1)/2
  return A1

segm_img = np.full(grayImage.shape, 0)
A = []

for i in range(0, grayImage.shape[0], 5):
    for j in range(0, grayImage.shape[1], 5):
      tmp=getA(grayImage[i:i + 5, j: j + 5])
      A.append(tmp)
      #print(tmp)
      if tmp >= 1001:
          segm_img[i:i + 5,j:j + 5].fill(255)

cv2_imshow(segm_img)