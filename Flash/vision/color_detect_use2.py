#!/usr/bin/python3.8
import sys
ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'

if ros_path in sys.path:

    sys.path.remove(ros_path)

import cv2
import numpy as np
import joblib
import matplotlib.pyplot as plt
import time

sys.path.append("..")
import communication

model_path = '/home/lt/mofang/model/svm_cube_10*10_up2.model'
img_path = '/home/lt/mofang/view2/test.jpg'
clf = joblib.load(model_path) # 加载模型

point1_x = 187
point1_y = 321
point2_x = 190
point2_y = 251
point3_x = 195
point3_y = 182

point4_x = 222
point4_y = 332
point5_x = 226
point5_y = 254
point6_x = 232
point6_y = 177

point7_x = 270
point7_y = 349
point8_x = 276
point8_y = 261
point9_x = 279
point9_y = 171

point10_x = 337
point10_y = 356
point11_x = 345
point11_y = 272
point12_x = 350
point12_y = 174

point13_x = 392
point13_y = 346
point14_x = 400
point14_y = 266
point15_x = 400
point15_y = 190

point16_x = 432
point16_y = 340
point17_x = 437
point17_y = 274
point18_x = 440
point18_y = 199
 
def read_usb_capture():
    # 选择摄像头的编号
    cap = cv2.VideoCapture(1)
    cap.set(10,-10) #0
    cap.set(11,10) #50
    cap.set(12,64) #64
    cap.set(13,0) #0
    cap.set(14,64) #64
    # 添加这句是可以用鼠标拖动弹出的窗体
    cv2.namedWindow('real_img', cv2.WINDOW_NORMAL)
    while(cap.isOpened()):
        # 读取摄像头的画面
        ret, frame = cap.read()
        # 真实图
        cv2.rectangle(frame,(point1_x-7,point1_y-7),(point1_x + 7,point1_y + 7),(0,255,0))
        cv2.rectangle(frame,(point2_x-7,point2_y-7),(point2_x + 7,point2_y + 7),(0,255,0))
        cv2.rectangle(frame,(point3_x-7,point3_y-7),(point3_x + 7,point3_y + 7),(0,255,0))
        cv2.rectangle(frame,(point4_x-7,point4_y-7),(point4_x + 7,point4_y + 7),(0,255,0))
        cv2.rectangle(frame,(point5_x-7,point5_y-7),(point5_x + 7,point5_y + 7),(0,255,0))
        cv2.rectangle(frame,(point6_x-7,point6_y-7),(point6_x + 7,point6_y + 7),(0,255,0))
        cv2.rectangle(frame,(point7_x-7,point7_y-7),(point7_x + 7,point7_y + 7),(0,255,0))
        cv2.rectangle(frame,(point8_x-7,point8_y-7),(point8_x + 7,point8_y + 7),(0,255,0))
        cv2.rectangle(frame,(point9_x-7,point9_y-7),(point9_x + 7,point9_y + 7),(0,255,0))

        cv2.rectangle(frame,(point10_x-7,point10_y-7),(point10_x + 7,point10_y + 7),(0,255,0))
        cv2.rectangle(frame,(point11_x-7,point11_y-7),(point11_x + 7,point11_y + 7),(0,255,0))
        cv2.rectangle(frame,(point12_x-7,point12_y-7),(point12_x + 7,point12_y + 7),(0,255,0))
        cv2.rectangle(frame,(point13_x-7,point13_y-7),(point13_x + 7,point13_y + 7),(0,255,0))
        cv2.rectangle(frame,(point14_x-7,point14_y-7),(point14_x + 7,point14_y + 7),(0,255,0))
        cv2.rectangle(frame,(point15_x-7,point15_y-7),(point15_x + 7,point15_y + 7),(0,255,0))
        cv2.rectangle(frame,(point16_x-7,point16_y-7),(point16_x + 7,point16_y + 7),(0,255,0))
        cv2.rectangle(frame,(point17_x-7,point17_y-7),(point17_x + 7,point17_y + 7),(0,255,0))
        cv2.rectangle(frame,(point18_x-7,point18_y-7),(point18_x + 7,point18_y + 7),(0,255,0))
        cv2.imshow('real_img', frame)
        # 按下'q'就退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            communication.send_msg('LC RC\r\n')
            cv2.imwrite(img_path,frame)
            cap.release()
            cv2.destroyAllWindows()
    return frame

def img2vector(img):
 
    img_arr = np.array(img) 
    img_normlization = img_arr/255 
    img_arr2 = np.reshape(img_normlization, (1,-1)) 
    return img_arr2

def detect_color():
    st = time.perf_counter()
    img = read_usb_capture()

    ROI1 = img[point1_y - 5:point1_y + 5, point1_x - 5:point1_x + 5]
    ROI2 = img[point2_y - 5:point2_y + 5, point2_x - 5:point2_x + 5]
    ROI3 = img[point3_y - 5:point3_y + 5, point3_x - 5:point3_x + 5]
    ROI4 = img[point4_y - 5:point4_y + 5, point4_x - 5:point4_x + 5]
    ROI5 = img[point5_y - 5:point5_y + 5, point5_x - 5:point5_x + 5]
    ROI6 = img[point6_y - 5:point6_y + 5, point6_x - 5:point6_x + 5]
    ROI7 = img[point7_y - 5:point7_y + 5, point7_x - 5:point7_x + 5]
    ROI8 = img[point8_y - 5:point8_y + 5, point8_x - 5:point8_x + 5]
    ROI9 = img[point9_y - 5:point9_y + 5, point9_x - 5:point9_x + 5]

    ROI10 = img[point10_y - 5:point10_y + 5, point10_x - 5:point10_x + 5]
    ROI11 = img[point11_y - 5:point11_y + 5, point11_x - 5:point11_x + 5]
    ROI12 = img[point12_y - 5:point12_y + 5, point12_x - 5:point12_x + 5]
    ROI13 = img[point13_y - 5:point13_y + 5, point13_x - 5:point13_x + 5]
    ROI14 = img[point14_y - 5:point14_y + 5, point14_x - 5:point14_x + 5]
    ROI15 = img[point15_y - 5:point15_y + 5, point15_x - 5:point15_x + 5]
    ROI16 = img[point16_y - 5:point16_y + 5, point16_x - 5:point16_x + 5]
    ROI17 = img[point17_y - 5:point17_y + 5, point17_x - 5:point17_x + 5]
    ROI18 = img[point18_y - 5:point18_y + 5, point18_x - 5:point18_x + 5]
    
    img2arr1 = img2vector(ROI1)
    img2arr2 = img2vector(ROI2)
    img2arr3 = img2vector(ROI3)
    img2arr4 = img2vector(ROI4)
    img2arr5 = img2vector(ROI5)
    img2arr6 = img2vector(ROI6)
    img2arr7 = img2vector(ROI7)
    img2arr8 = img2vector(ROI8)
    img2arr9 = img2vector(ROI9)

    img2arr10 = img2vector(ROI10)
    img2arr11 = img2vector(ROI11)
    img2arr12 = img2vector(ROI12)
    img2arr13 = img2vector(ROI13)
    img2arr14 = img2vector(ROI14)
    img2arr15 = img2vector(ROI15)
    img2arr16 = img2vector(ROI16)
    img2arr17 = img2vector(ROI17)
    img2arr18 = img2vector(ROI18)

    
    preResult1 = clf.predict(img2arr1)
    preResult2 = clf.predict(img2arr2)
    preResult3 = clf.predict(img2arr3)
    preResult4 = clf.predict(img2arr4)
    preResult5 = clf.predict(img2arr5)
    preResult6 = clf.predict(img2arr6)
    preResult7 = clf.predict(img2arr7)
    preResult8 = clf.predict(img2arr8)
    preResult9 = clf.predict(img2arr9)

    preResult10 = clf.predict(img2arr10)
    preResult11 = clf.predict(img2arr11)
    preResult12 = clf.predict(img2arr12)
    preResult13 = clf.predict(img2arr13)
    preResult14 = clf.predict(img2arr14)
    preResult15 = clf.predict(img2arr15)
    preResult16 = clf.predict(img2arr16)
    preResult17 = clf.predict(img2arr17)
    preResult18 = clf.predict(img2arr18)


    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    print(preResult1,preResult2,preResult3,'  ',preResult10,preResult11,preResult12)
    print(preResult4,preResult5,preResult6,'  ',preResult13,preResult14,preResult15)
    print(preResult7,preResult8,preResult9,'  ',preResult16,preResult17,preResult18)
    
    et = time.perf_counter()
    print("spent {:.4f}s.".format((et - st)))
    # plt.imshow(img)
    # plt.show()
    color_state1 = preResult1[0]+preResult2[0]+preResult3[0]+preResult4[0]+preResult5[0]+preResult6[0]+preResult7[0]+preResult8[0]+preResult9[0]
    color_state2 = preResult10[0]+preResult11[0]+preResult12[0]+preResult13[0]+preResult14[0]+preResult15[0]+preResult16[0]+preResult17[0]+preResult18[0]
    return color_state1,color_state2

if __name__ == '__main__':  
    #read_usb_capture()
    detect_color()