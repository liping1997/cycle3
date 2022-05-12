import cv2
import os
import torch
import numpy as np




def cutimg(img, num=25,overlap_factor=128):


    """a,b,c,d,分别存储A,B1,B2,B3的256*256块"""
    factor = int(np.sqrt(num))
    x=6
    a=[]

    b=[]

    for i in range(factor):
        a1 = []
        b1 = []
        for ii in range(factor):
            img_temp1 = img[i * overlap_factor:(i + 2) * overlap_factor, ii * overlap_factor:(ii + 2) * overlap_factor]
            img_temp2 = img[i * overlap_factor:(i + 2) * overlap_factor, (ii+x) * overlap_factor:(ii +x+2) * overlap_factor]
            # print(i)
            # print(img_temp1.shape,img_temp2.shape,img_temp3.shape,img_temp4.shape)
            a1.append(img_temp1)
            b1.append(img_temp2)

        a.append(a1)
        b.append(b1)

    return a,b

# img=cv2.imread('./data_test/173.jpg')
# a,b,c,d=cutimg(img,9)
# for i in range(9):
#     img=np.hstack((a[i],b[i],c[i],d[i]))
#     cv2.imwrite('./save/{}.jpg'.format(i),img)

# img=cv2.imread('./0.jpg')
# a,b,c,d=cutimg(img,25)
# cv2.imshow('1',a[2])
# cv2.waitKey(0)