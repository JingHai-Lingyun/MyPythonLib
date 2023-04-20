#导入库
import cv2,os,time
import numpy as np

# 视频导出图片操作
def video2img(videoname,delaytime):
    #初始化
    video = cv2.VideoCapture(videoname)
    fps = video.get(cv2.CAP_PROP_FPS)
    if not os.path.exists('lyOutput'):
        os.mkdir('lyOutput') # 创建文件夹

    #循环
    while True:
        # 读图+处理+显示
        ok,image = video.read() # 原图  
        if not ok:
            break
        image = cv2.resize(image,(128,64)) # 调大小
        gray = cv2.cvtColor(image,6) # 转灰度
        bzy,binary = cv2.threshold(gray,120,255,1) # 转二值
        cv2.imshow('image',image)
        cv2.imshow('binary',binary)
        # 保存
        name = time.strftime('lyOutput/%H%M%S.jpg')
        cv2.imwrite(name,binary)
        # 退出检测
        if cv2.waitKey(delaytime)>0:
            break
    video.release()
    cv2.destroyAllWindows()

# 图片转文件操作
def img2txt(imgname,txtname):
    # 初始化
    if not os.path.exists('lyOutput'):
        os.mkdir('lyOutput') # 创建文件夹
    # 读图+处理
    image = cv2.imread(imgname,0)
    coords = np.where(image==255) # 提取二值图上所有为255的坐标
    coords = np.array(coords).T
    xy = [(j,i) for i,j in coords]  
    # 把数据存为文件
    f = open('lyOutput/'+txtname,'w',encoding='utf-8')
    f.write(str(xy))
    f.close()

# Author：林聪锦    