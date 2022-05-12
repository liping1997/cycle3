import os
import cv2
import numpy as np


# for i in os.listdir('./datasets/train'):
#     if 'A' in i:
#         path1=os.path.join('./datasets/train',i)
#         j=i.replace('A','B')
#         path2=os.path.join('./datasets/train',j)
#         img1=cv2.imread(path1)
#         img2=cv2.imread(path2)
#         img=np.hstack((img1,img2))
#         cv2.imwrite('./datasets/train/{}.jpg'.format(a),img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#         os.remove(path1)
#         os.remove(path2)
#         a=a+1
#         print(a)
#





# class Solution:
#     def singleNumber(self, nums) :
#         dic=dict()
#         for i in nums:
#             if i not in dic:
#                 dic[i]=1
#             else:
#                 dic[i]=dic[i]+1
#         for (j,k)in dic.items():
#             if k==1:
#
#                 return j
#
# a=Solution()
# b=a.singleNumber([1,1,1,2,2,2,3,4,4,5,4,5,5])
# print(b)

# for i in os.listdir('./datasets/test'):
#     path=os.path.join('./datasets/test',i)
#     img=cv2.imread(path)
#     img1=img[0][0][0]
#     img2 = img[0][511][0]
#     img3 = img[511][0][0]
#     img4 = img[511][511][0]
#     if img1==0 and img2==0 and img3==0 and img4==0:
#         os.remove(path)
#         print(a)
#         a=a+1

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         # 双指针法
#         A = True
#         B = True
#         for i in range(int(len(s) / 2)):
#             print(i)
#             if s[i] != s[len(s) - i - 1]:
#                 print(1)
#                 for j in range(i + 1, int(len(s) / 2)):
#                     print(j)
#                     if s[j] != s[len(s) - j]:
#
#                         A = False
#                         break
#                 print(2)
#                 for k in range(i, int(len(s) / 2)):
#                     if s[k] != s[len(s) - k - 2]:
#                         B = False
#                         break
#                 print(3)
#                 break
#         if A == False and B == False:
#             return False
#
#         return True
# #
# #
# A=Solution()
# bool1=A.validPalindrome("eabce")
# print(bool1)
#*******************************************************************************************************
# a=0                                                                                                 #*
# for i in os.listdir('./test'):                                                                      #*
#     if 'A' in i :                                                                                   #*
#         path=os.path.join('./test',i)
#         path1=path.replace('A.','B.')
#         img1=cv2.imread(path)
#         img2=cv2.imread(path1)
#         img3=np.hstack((img1,img2))
#         cv2.imwrite('./test/{}.jpg'.format(a),img3,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#         os.remove(path1)
#         os.remove(path)
#         a=a+1
#***********************************************************************************************************

# def aaaa():
#     a=4
#     def backtrack(index):
#
#
#
#         a=a+1
#         print(a,id(a))
#         if index>5:
#             return
#         backtrack(index+1)
#
#         print(a,id(a))
#     backtrack(0)


# for i in os.listdir('./results/FFA/test_latest/images'):
#     if "_fake_B" in i:
#         img=cv2.imread('./results/FFA/test_latest/images/{}'.format(i))
#
#         path=os.path.join('./results/',i.replace('_fake_B',""))
#         cv2.imwrite(path,img)

img=cv2.imread('480.jpg')
img1=cv2.imread('A0_fake_B.png')
img2=np.hstack((img,img1))
cv2.imwrite('2.jpg',img2,[int(cv2.IMWRITE_JPEG_QUALITY),100])