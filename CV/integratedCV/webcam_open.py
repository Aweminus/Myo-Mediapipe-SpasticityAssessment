from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#import time
import cv2
#import mediapipe as mp
import numpy as np
#mp_drawing = mp.solutions.drawing_utils
#mp_pose = mp.solutions.pose

class webcam_capture(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        #Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #self.ThreadActive = True
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        #with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while Capture.isOpened():
        #while self.ThreadActive == True:
                ret, frame = Capture.read()
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Recolor image to RGB
                    #image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    #image.flags.writeable = False

                # Make detection
                    #results = pose.process(image)

                # Recolor back to BGR
                    #image.flags.writeable = True
                    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                    ConvertToQtFormat = QImage(image.data, image.shape[1], image.shape[0],
                                               QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                    

    def stop1(self):

        #self.ThreadActive = False
        cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #print("1")

    def stop2(self):
        #self.ThreadActive = False
        cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #print("2")
