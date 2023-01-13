from flask import Flask, render_template, Response
from use_yolo import yoloing
import cv2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen():
    while True:
        image = yoloing()
        # 生成器迭代
        for i in image:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + i + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
