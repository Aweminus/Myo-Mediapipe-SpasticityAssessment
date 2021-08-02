from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
import global_var
import statistics


class webcam_apply_mediapipe_right(QThread):
    ImageUpdate = pyqtSignal(QImage)
    
    def calculate_angle(self,a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    def run(self):

        global Active,Final_Velocity,anglerec,timerec,velocityrecFlt
        Active = 1
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        angle_right_old=0
        velocityFlt=0

        anglerec=[]
        timerec=[]
        velocityrec = []
        velocityrecFlt = []

        Final_Velocity=0
        count=0
        angle_right_new=0

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            #while Capture.isOpened():
            while Active==1:
                ret, frame = Capture.read()
                timeNew=time.time()
                if count==0:
                    timeStart = timeNew
                    timeOld = timeStart
                if ret:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Recolor image to RGB
                #image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False

                # Make detection
                    results = pose.process(image)

                # Recolor back to BGR
                    image.flags.writeable = True
                    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks
                    try:
                        landmarks = results.pose_landmarks.landmark
                       # print("a")

                    # Get coordinates
                    # Left
                        shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                        wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                  landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    # Right
                        shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                        wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                   landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                    # Calculate angle
                        angle_left = self.calculate_angle(shoulder_left, elbow_left, wrist_left)
                        #angle_left_new = angle_left
                        #print("angle_left")
                        angle_right = self.calculate_angle(shoulder_right, elbow_right, wrist_right)
                        #print("angle right")
                        angle_right_new=angle_right

                    # Visualize angle
                    # Visualize the left angle
                        cv2.putText(image, str(angle_left),
                                tuple(np.multiply(elbow_left, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )
                    # Visualize the right angle
                        cv2.putText(image, str(angle_right),
                                tuple(np.multiply(elbow_right, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    except:
                        pass

                # Render detections
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )


                    ConvertToQtFormat = QImage(image.data, image.shape[1], image.shape[0],
                                               QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                    
                    # ========================= Compute Velocity =========================
                    anglerec.append(angle_right_new)
                    timerec.append(timeNew)

                    if count>=1:
                        velocityNew = abs(angle_right_new - angle_right_old) / abs(timerec[count]-timerec[count-1])
                        velocityrec.append(velocityNew)
                        #print(timerec[count]-timerec[count-1])
                    velocityrecLength = len(velocityrec)



                    # ---------------------- Moving Avg Filter ----------------------
                    velocityMedianList = []

                    if (velocityrecLength > 10):
                        for i in range(1, 11):
                            velocityMedianList.append(velocityrec[velocityrecLength - i])
                        velocityFlt = statistics.median(velocityMedianList)
                        velocityrecFlt.append(velocityFlt)

                    #print(velocityFlt)

                    angle_right_old = angle_right_new
                    count+=1


    def stop1(self):
        Active = 0
        cv2.VideoCapture(0, cv2.CAP_DSHOW).release()

        Final_Velocity=0
        prevVelocity=0

        velocityMedianLength = len(velocityrecFlt)
        startCount = 0
        startIndex = 0
        endIndex = 0

        for i in range(0, velocityMedianLength - 1):
            currVelocity = velocityrecFlt[i]
            if i>0:
                prevVelocity = velocityrecFlt[i - 1]
            # if (currVelocity > 5 & velocityrec[i-1]<5 & i < 300):
            if ((currVelocity > 30) & (startCount == 0) & (i > 10)):
                startIndex = i
                startCount = startCount + 1
            if ((currVelocity < 30) & (prevVelocity > 30)):
                endIndex = i

        print("==========================================================")
        print(startIndex)
        print(endIndex)
        print("==========================================================")

        num = 0
        Final_Velocity_Sum = 0
        for c in range(startIndex, endIndex):
            Final_Velocity_Sum = Final_Velocity_Sum + velocityrecFlt[c]
            num = num + 1
        if num!=0:
            Final_Velocity = Final_Velocity_Sum / num
        global_var.set_value('Final_Velocity', Final_Velocity)
        print('The average velocity is' , Final_Velocity)

    def stop2(self):
        cv2.VideoCapture(0, cv2.CAP_DSHOW).release()
