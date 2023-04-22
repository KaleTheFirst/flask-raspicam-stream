import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

# while True:
sensor=GPIO.input(11)




class RPiCamera(object):

    def __init__(self):
        self.stream = PiVideoStream().start()
        time.sleep(2.0)

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        frame = self.stream.read()

        result, jpeg = cv2.imencode('.jpg', frame)

        if sensor==0:                 
            print("Nothing seen"),sensor

        elif sensor==1:               
            print("I see you"),sensor




        return jpeg.tobytes()