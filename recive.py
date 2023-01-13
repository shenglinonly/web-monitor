import socket
import cv2
import io
from PIL import Image
import numpy as np


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(("0.0.0.0", 9090))


def rec():
    while True:
        data, ip = s.recvfrom(100000)
        bytes_stream = io.BytesIO(data)
        image = Image.open(bytes_stream)
        img_1 = np.asarray(image)
        img_2 = cv2.cvtColor(img_1, cv2.COLOR_RGB2BGR)  # ESP32采集的是RGB格式，要转换为BGR（opencv的格式）
        img_3 = cv2.flip(img_2, 1)  # 镜像翻转
        yield img_3
