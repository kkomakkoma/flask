import cv2
from time import time

class VideoStream(object):
    def __init__(self):
        self.video=cv2.VideoCapture('/var/www/flask/static/uploads/mov_bbb.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
        

