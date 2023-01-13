# 鹰眼智能监控检测系统



>**本项目采用 esp32-cam + micropython + flask + yolo 格式, 打造web视频监控和目标检测**



## 介绍

- 硬件: ESP32-CAM是一个开发板, 双核, 性能强悍，它上面集成了Camera摄像头模块.

- 软件: 在esp32-cam上用到了micro python进行编写, flask框架搭建浏览器界面, yolo实现目标检测.



项目框架

```
│  app.py  # flask 框架
│  README.md 
│  recive.py  # 接受数据
│  use_yolo.py # 使用yolo目标检测
│  yolo_fastest.py  # yolo检测代码
│
│
├─cfg  # yolo配置文件
│      coco.names
│      yolo-fastest-xl-coco.cfg
│      yolo-fastest-xl-coco.weights
│      yolo-fastest-xl.cfg
│      yolo-fastest-xl.weights
│      yolo-fastest.cfg
│      yolo-fastest.weights
│      yolov3.cfg
│      yolov3.weights
│
├─static  # flask静态文件
│  ├─css
│  │      hello.css
│  │
│  └─images
│          favicon.icol
│
├─templates  # flask静态模板
      index.html
```

