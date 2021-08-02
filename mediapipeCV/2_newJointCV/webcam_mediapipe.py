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


class webcam_apply_mediapipe(QThread):
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

        #velocity=0
        angle_left_old=0
        anglerec=[]
        timerec=[]
        #velocity_sum=0
        #timeStart=time.time()
        #timeOld=timeStart
        velocityrec = []
        velocityrecFlt = []
        velocityFlt = 0
        timeOld=0
        Final_Velocity=0
        count=0
        angle_left_new=0

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            #while Capture.isOpened():
            while Active==1:
                ret, frame = Capture.read()
                timeNew=time.time()
                if count == 0:
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
                        angle_left_new = angle_left
                        #print("angle_left")
                        angle_right = self.calculate_angle(shoulder_right, elbow_right, wrist_right)
                        #print("angle right")

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
                    
                    # if  timeNew > (timeOld + 0.01) :
                    #     velocityNew  = (angle_left_new - angle_left_old)/0.01;
                    #     velocity.append(velocity[count] * 0.8 + velocityNew * 0.2);
                    #     angle_left_old= angle_left_new;
                    #     count+=1
                    #     timeOld=timeNew

                    # ========================= Compute Velocity =========================
                    anglerec.append(angle_left_new)
                    timerec.append(timeNew)
                    #if (timeOld!=timeNew):
                    if count>=1:
                        velocityNew = abs(angle_left_new - angle_left_old) / abs(timerec[count]-timerec[count-1])
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

                    angle_left_old = angle_left_new
                    timeOld = timeNew
                    count+=1
                    #print(velocityFlt)


                    # if timeNew>(timeOld+0.01):
                    #     velocityNew=(angle_left_new - angle_left_old)/0.01;
                    #     velocity= velocity * 0.8 + velocityNew * 0.2;
                    #     #print(velocity)
                    #
                    #     if timeNew>(timeFirst+0.5):
                    #         if velocity>10:
                    #             #number=0
                    #             anglerec.append(angle_left_new)
                    #             #print("a")
                    #             #number+=1
                    #             timerec.append(timeNew)
                    #
                    #             #if velocity<=5:
                    #                 #break2 = True
                    #                 #print("2")
                    #                 #break
                    #         #if (break2):
                    #         #    break
                    #     angle_left_old=angle_left_new
                    #     count+=1
                    #     timeOld=timeNew


                    #if cv2.waitKey(10) & 0xFF == ord('q'):
                    #if stop==1:
                        #break
            #num=0
            #print(num)
            #for i in range(count-100):
            #    velocity_sum+=velocity[50+i]
            #    num+=1
            #Final_Velocity=float(velocity_sum)/float(num)
            #print(Final_Velocity)
        #self.ThreadActive = False
        #cv2.VideoCapture(0, cv2.CAP_DSHOW).release()
            #print("0")
            #Capture.release()
            #cap.release()

            #self.quit()
    def stop1(self):
        #stop=1
        Active = 0
        # num=0
        # velocity_sum=0
        cv2.VideoCapture(0, cv2.CAP_DSHOW).release()

        print("left")

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

        # Final_Velocity = abs(anglerec[endIndex+10] - anglerec[startIndex+10]) / (timerec[endIndex+10] - timerec[startIndex+10])
        num = 0
        Final_Velocity_Sum = 0
        for c in range(startIndex, endIndex):
            Final_Velocity_Sum = Final_Velocity_Sum + velocityrecFlt[c]
            num = num + 1
        if num!=0:
            Final_Velocity = Final_Velocity_Sum / num
        global_var.set_value('Final_Velocity', Final_Velocity)
        print('The average velocity is' , Final_Velocity)

        # for i in range(count-50):
        #     if velocity[i]>5:
        #         velocity_sum+=velocity[50+i]
        #         num+=1
        # if num!=0:
        #     Final_Velocity=float(velocity_sum)/num
        # Final_Velocity=(anglerec[-1]-anglerec[0])/(timerec[-1]-timerec[0])
        # print(Final_Velocity)

        # #print("0")
        # cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #cv2.destroyAllWindows()
        #cv2.destroyAllWindows()
        #print("1")

        #return Final_Velocity
        #sys.exit()

    # def stop2(self):
    #     #self.ThreadActive = False
    #     cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
    #     cv2.destroyAllWindows()
    #     print("2")
        #cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
        #num=0
        #for i in range(1000):
        #    velocity_sum+=velocity[50+i]
        #    num+=1
        #    Final_Velocity=float(velocity_sum)/num
        #print(Final_Velocity)
        #cap.release()
        #cv2.destroyAllWindows()
        #self.quit()
    def stop2(self):
        cv2.VideoCapture(0, cv2.CAP_DSHOW).release()