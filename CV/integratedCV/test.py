# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget)
# from PyQt5.Qt import Qt
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#
#     # def keyPressEvent(self, event):
#     #     if event.key() == Qt.Key_Space:
#     #         self.test_method()
#     #
#     # def test_method(self):
#     #     print('Space key pressed')
#     def keyPressEvent(self, event):
#             print(event.key())
#
#             if (event.key() == 16777220 or event.key() == 16777221):
#                     print("ok")
#                     print("回车")
#             if event.key() == Qt.AltModifier:
#                     print("alt")
#             if event.key() == Qt.Key_Space:
#                     print("空格")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     demo = MainWindow()
#     demo.show()
#
#     sys.exit(app.exec_())


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
# import sys
# import cv2
#
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import QPalette, QBrush, QPixmap
# import os
#
#
# class Ui_MainWindow(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(Ui_MainWindow, self).__init__(parent)
#
#         # self.face_recong = face.Recognition()
#         self.timer_camera = QtCore.QTimer()
#         self.cap = cv2.VideoCapture()
#         self.CAM_NUM = 0
#         self.set_ui()
#         self.slot_init()
#         self.__flag_work = 0
#         self.x = 0
#         self.count = 0
#
#     def set_ui(self):
#
#         self.__layout_main = QtWidgets.QHBoxLayout()
#         self.__layout_fun_button = QtWidgets.QVBoxLayout()
#         self.__layout_data_show = QtWidgets.QVBoxLayout()
#
#         self.button_open_camera = QtWidgets.QPushButton(u'打开相机')
#
#         self.button_close = QtWidgets.QPushButton(u'退出')
#
#         # Button 的颜色修改
#         button_color = [self.button_open_camera, self.button_close]
#         for i in range(2):
#             button_color[i].setStyleSheet("QPushButton{color:black}"
#                                           "QPushButton:hover{color:red}"
#                                           "QPushButton{background-color:rgb(78,255,255)}"
#                                           "QPushButton{border:2px}"
#                                           "QPushButton{border-radius:10px}"
#                                           "QPushButton{padding:2px 4px}")
#
#         self.button_open_camera.setMinimumHeight(50)
#         self.button_close.setMinimumHeight(50)
#
#         # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
#         self.move(500, 500)
#
#         # 信息显示
#         self.label_show_camera = QtWidgets.QLabel()
#         self.label_move = QtWidgets.QLabel()
#         self.label_move.setFixedSize(100, 100)
#
#         self.label_show_camera.setFixedSize(641, 481)
#         self.label_show_camera.setAutoFillBackground(False)
#
#         self.__layout_fun_button.addWidget(self.button_open_camera)
#         self.__layout_fun_button.addWidget(self.button_close)
#         self.__layout_fun_button.addWidget(self.label_move)
#
#         self.__layout_main.addLayout(self.__layout_fun_button)
#         self.__layout_main.addWidget(self.label_show_camera)
#
#         self.setLayout(self.__layout_main)
#         self.label_move.raise_()
#         self.setWindowTitle(u'摄像头')
#
#         '''
#         # 设置背景图片
#         palette1 = QPalette()
#         palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
#         self.setPalette(palette1)
#         '''
#
#     def slot_init(self):
#         self.button_open_camera.clicked.connect(self.button_open_camera_click)
#         self.timer_camera.timeout.connect(self.show_camera)
#         self.button_close.clicked.connect(self.close)
#
#     def button_open_camera_click(self):
#         if self.timer_camera.isActive() == False:
#             flag = self.cap.open(self.CAM_NUM)
#             if flag == False:
#                 msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
#                                                     buttons=QtWidgets.QMessageBox.Ok,
#                                                     defaultButton=QtWidgets.QMessageBox.Ok)
#             # if msg==QtGui.QMessageBox.Cancel:
#             #                     pass
#             else:
#                 self.timer_camera.start(30)
#
#                 self.button_open_camera.setText(u'关闭相机')
#         else:
#             self.timer_camera.stop()
#             self.cap.release()
#             self.label_show_camera.clear()
#             self.button_open_camera.setText(u'打开相机')
#
#     def show_camera(self):
#         flag, self.image = self.cap.read()
#         # face = self.face_detect.align(self.image)
#         # if face:
#         #     pass
#         show = cv2.resize(self.image, (640, 480))
#         show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
#         # print(show.shape[1], show.shape[0])
#         # show.shape[1] = 640, show.shape[0] = 480
#         showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
#         self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
#         # self.x += 1
#         # self.label_move.move(self.x,100)
#
#         # if self.x ==320:
#         #     self.label_show_camera.raise_()
#
#     def closeEvent(self, event):
#         ok = QtWidgets.QPushButton()
#         cacel = QtWidgets.QPushButton()
#
#         msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")
#
#         msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
#         msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
#         ok.setText(u'确定')
#         cacel.setText(u'取消')
#         # msg.setDetailedText('sdfsdff')
#         if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
#             event.ignore()
#         else:
#             #             self.socket_client.send_command(self.socket_client.current_user_command)
#             if self.cap.isOpened():
#                 self.cap.release()
#             if self.timer_camera.isActive():
#                 self.timer_camera.stop()
#             event.accept()
#
#
# if __name__ == "__main__":
#     App = QApplication(sys.argv)
#     ex = Ui_MainWindow()
#     ex.show()
#     sys.exit(App.exec_())
#


# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
# from PyQt5.QtGui import QPixmap
# import sys
# import cv2
# from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
# import numpy as np
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
#
#
#
# class VideoThread(QThread):
#     change_pixmap_signal = pyqtSignal(np.ndarray)
#
#     def __init__(self):
#         super().__init__()
#         self._run_flag = True
#
#     def calculate_angle(a, b, c):
#         a = np.array(a)  # First
#         b = np.array(b)  # Mid
#         c = np.array(c)  # End
#
#         radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
#         angle = np.abs(radians * 180.0 / np.pi)
#
#         if angle > 180.0:
#             angle = 360 - angle
#
#         return angle
#
#     def run(self):
#         # capture from web cam
#         cap = cv2.VideoCapture(0)
#         with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#             while self._run_flag:
#                 ret, cv_img = cap.read()
#                 #if ret:
#                 self.change_pixmap_signal.emit(cv_img)
#             # # Recolor image to RGB
#             #     image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
#             #     image.flags.writeable = False
#             #
#             # # Make detection
#             #     results = pose.process(image)
#             #
#             # # Recolor back to BGR
#             #     image.flags.writeable = True
#             #     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#             #
#             # # Extract landmarks
#             #     try:
#             #         landmarks = results.pose_landmarks.landmark
#             #
#             #     # Get coordinates
#             #     # Left
#             #         shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
#             #                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
#             #         elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
#             #                   landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
#             #         wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
#             #                   landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
#             #
#             #     # Right
#             #         shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
#             #                       landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
#             #         elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
#             #                    landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
#             #         wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
#             #                    landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
#             #
#             #     # Calculate angle
#             #         angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
#             #         angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)
#             #
#             #     # Visualize angle
#             #     # Visualize the left angle
#             #         cv2.putText(image, str(angle_left),
#             #                 tuple(np.multiply(elbow_left, [640, 480]).astype(int)),
#             #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#             #                 )
#             #     # Visualize the right angle
#             #         cv2.putText(image, str(angle_right),
#             #                 tuple(np.multiply(elbow_right, [640, 480]).astype(int)),
#             #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#             #                 )
#             #
#             #     except:
#             #         pass
#             #
#             # # Render detections
#             # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#             #                           mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
#             #                           mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
#             #                           )
#             #
#             # cv2.imshow('Mediapipe Feed', image)
#         # shut down capture system
#         #cap.release()
#         #cv2.destroyAllWindows()
#
#     def stop(self):
#         """Sets run flag to False and waits for thread to finish"""
#         self._run_flag = False
#         self.wait()
#
#
# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Qt live label demo")
#         self.disply_width = 640
#         self.display_height = 480
#         # create the label that holds the image
#         self.image_label = QLabel(self)
#         self.image_label.resize(self.disply_width, self.display_height)
#         # create a text label
#         self.textLabel = QLabel('Webcam')
#
#         # create a vertical box layout and add the two labels
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.image_label)
#         vbox.addWidget(self.textLabel)
#         # set the vbox layout as the widgets layout
#         self.setLayout(vbox)
#
#         # create the video capture thread
#         self.thread = VideoThread()
#         # connect its signal to the update_image slot
#         #self.thread.change_pixmap_signal.connect(self.update_image)
#
#         self.update_image
#         # start the thread
#         self.thread.start()
#
#     def closeEvent(self, event):
#         self.thread.stop()
#         event.accept()
#
#     @pyqtSlot(np.ndarray)
#     def update_image(self, cv_img):
#         """Updates the image_label with a new opencv image"""
#         qt_img = self.convert_cv_qt(cv_img)
#         self.image_label.setPixmap(qt_img)
#
#     def convert_cv_qt(self, cv_image):
#         with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
#             """Convert from an opencv image to QPixmap"""
#             image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
#             #image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)
#             image.flags.writeable = False
#
#         # Make detection
#             results = pose.process(image)
#
#         # Recolor back to BGR
#             image.flags.writeable = True
#             #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#
#         # Extract landmarks
#             try:
#                 landmarks = results.pose_landmarks.landmark
#
#             # Get coordinates
#             # Left
#                 shoulder_left = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
#                              landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
#                 elbow_left = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
#                           landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
#                 wrist_left = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
#                           landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
#
#             # Right
#                 shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
#                               landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
#                 elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
#                            landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
#                 wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
#                            landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
#
#             # Calculate angle
#                 angle_left = calculate_angle(shoulder_left, elbow_left, wrist_left)
#                 angle_right = calculate_angle(shoulder_right, elbow_right, wrist_right)
#
#             # Visualize angle
#             # Visualize the left angle
#                 cv2.putText(image, str(angle_left),
#                         tuple(np.multiply(elbow_left, [640, 480]).astype(int)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#                         )
#             # Visualize the right angle
#                 cv2.putText(image, str(angle_right),
#                         tuple(np.multiply(elbow_right, [640, 480]).astype(int)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
#                         )
#
#             except:
#                 pass
#
#         # Render detections
#             mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
#                                   mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
#                                   mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
#                                   )
#
#             #cv2.imshow('Mediapipe Feed', image)
#             h, w, ch = image.shape
#             bytes_per_line = ch * w
#             convert_to_Qt_format = QtGui.QImage(image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
#             p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
#             return QPixmap.fromImage(p)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     a = App()
#     a.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    def ImageUpdateSlot(self, image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(image))

    def CancelFeed(self):
        self.Worker1.stop()


class Worker1(QThread):
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
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.ThreadActive:
                ret, frame = Capture.read()
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

                #cv2.imshow('Mediapipe Feed', image)
                    #FlippedImage = cv2.flip(image, 1)
                    #ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)

                    ConvertToQtFormat = QImage(image.data, image.shape[1], image.shape[0],
                                               QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())

