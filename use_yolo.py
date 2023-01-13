from yolo_fastest import yolo_detect

import cv2

from recive import rec

label_path = './cfg/coco.names'
config_path = './cfg/yolo-fastest-xl-coco.cfg'
weights_path = './cfg/yolo-fastest-xl-coco.weights'

# 加载类别标签文件
LABELS = open(label_path).read().strip().split("\n")
nclass = len(LABELS)

# 加载模型配置和权重文件
print('从硬盘加载YOLO......')
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)


def yoloing():
    img_4 = rec()  # 生成器对象
    for i in img_4:  # 生成器迭代
        img_5 = yolo_detect(old_img=i, LABELS=LABELS, nclass=nclass, net=net)  # yolo检测
        """数据处理(处理成可以流视频播放的数据)"""
        ret, jpeg = cv2.imencode('.jpg', img_5)
        image = jpeg.tobytes()
        yield image


