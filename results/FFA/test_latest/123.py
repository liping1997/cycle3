import os
import cv2
# import numpy as np
# a=0
# for i in os.listdir('./images'):
#     if '_fake_B' in i:
#         img=cv2.imread('./images/{}'.format(i))
#         A=i.replace('_fake_B.png','.jpg')
#         B1=A.replace('A','B1')
#         B2 = A.replace('A', 'B2')
#         B3 = A.replace('A', 'B3')
#
#         imgA=cv2.imread('./images/{}'.format(A))
#         imgB1 = cv2.imread('./images/{}'.format(B1))
#         imgB2 = cv2.imread('./images/{}'.format(B2))
#         imgB3 = cv2.imread('./images/{}'.format(B3))
#
#         I=np.hstack((imgA,imgB1,imgB2,imgB3,img))
#
#         cv2.imwrite('./result/{}.jpg'.format(a),I,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#         a+=1
#         print(a)


import cv2
import numpy as np
import os



def random_crop(input_img, crop_size):

    img_h, img_w, img_c = input_img.shape
    crop_h = np.random.randint(0, 512- crop_size)
    crop_w = np.random.randint(0, 512- crop_size)
    crop_h1 = np.random.randint(0, 512 - crop_size)
    crop_w1 = np.random.randint(0, 512 - crop_size)
    input_img0 = input_img[crop_h:crop_h + crop_size, crop_w:crop_w + crop_size, :]
    input_img1 = input_img[crop_h:crop_h+crop_size, crop_w+512:crop_w+crop_size+512, :]
    input_img2 = input_img[crop_h:crop_h + crop_size, crop_w+1024:crop_w + crop_size+1024, :]
    input_img3 = input_img[crop_h:crop_h + crop_size, crop_w+1536:crop_w+ crop_size+1536, :]
    input_img8 = input_img[crop_h:crop_h + crop_size, crop_w+2048:crop_w+ crop_size+2048, :]

    input_img4 = input_img[crop_h1:crop_h1 + crop_size, crop_w1:crop_w1 + crop_size, :]
    input_img5 = input_img[crop_h1:crop_h1 + crop_size, crop_w1 + 512:crop_w1 + crop_size + 512, :]
    input_img6 = input_img[crop_h1:crop_h1 + crop_size, crop_w1 + 1024:crop_w1 + crop_size + 1024, :]
    input_img7 = input_img[crop_h1:crop_h1 + crop_size, crop_w1 + 1536:crop_w1 + crop_size + 1536, :]
    input_img9 = input_img[crop_h1:crop_h1 + crop_size, crop_w1 + 2048:crop_w1 + crop_size + 2048, :]

    return input_img0,input_img1,input_img2,input_img3,input_img4,input_img5,input_img6,input_img7,input_img8,input_img9

a=0
for i in os.listdir('result'):
    path=os.path.join('./result',i)
    img=cv2.imread(path)
    img0,img1,img2,img3,img4,img5,img6,img7,img8,img9=random_crop(img,256)

    img8=np.hstack((img0,img1,img2,img3,img8))

    cv2.imwrite('./R/{}.jpg'.format(a),img8,[int(cv2.IMWRITE_WEBP_QUALITY),100])
    a=a+1
    if a%3==0:
        img9 = np.hstack((img4, img5, img6, img7,img9))
        cv2.imwrite('./R/{}.jpg'.format(a), img9, [int(cv2.IMWRITE_WEBP_QUALITY), 100])
        a = a + 1
        print(a)

