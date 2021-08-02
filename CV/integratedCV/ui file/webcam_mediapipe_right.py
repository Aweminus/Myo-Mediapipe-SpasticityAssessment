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

        global velocity,count,stop,Active,Final_Velocity
        Active = 1
        Capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        stop=0
        velocity=[0]
        angle_right_old=0
        #velocity_sum=0
        timeStart=time.time()
        timeOld=timeStart
        Final_Velocity=0
        count=0
        angle_right_new=0
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            #while Capture.isOpened():
            while Active==1:
                ret, frame = Capture.read()
                timeNew=time.time()
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
                    
                    if  timeNew > (timeOld + 0.01) :
                        velocityNew  = (angle_right_new - angle_right_old)/0.01;
                        velocity.append(velocity[count] * 0.8 + velocityNew * 0.2);
                        angle_right_old= angle_right_new;
                        count+=1
                        timeOld=timeNew
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
        num=0
        velocity_sum=0
        print("right")
        Final_Velocity=0
        for i in range(count-100):
            velocity_sum+=velocity[50+i]
            num+=1
        if num!=0:
            Final_Velocity=float(velocity_sum)/num
        print(Final_Velocity)
        global_var.set_value('Final_Velocity', Final_Velocity)
        #print("0")
        cv2.VideoCapture(0,cv2.CAP_DSHOW).release()
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
