import numpy as np
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        frame = cv2.rectangle(frame,(384-100,0+100),(510-100,128+100),(0,255,0),3)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
