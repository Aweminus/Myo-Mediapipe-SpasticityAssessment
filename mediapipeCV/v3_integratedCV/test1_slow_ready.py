# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1_slow_result.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from test1_medium_input import Ui_medium_input_1
from test1_slow_guidance import Ui_slow_guidance_1
from webcam_open import *
from webcam_mediapipe import *
import global_var

class Ui_slow_ready_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(125, 485, 750, 41))
        self.label_4.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 500, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 500, 61))
        self.label_2.setStyleSheet("font: 75 28pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(125, 550, 750, 31))
        self.label.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(825, 500, 81, 31))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(125, 125, 750, 350))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.btn_camera = QtWidgets.QPushButton(self.centralwidget)
        self.btn_camera.setGeometry(QtCore.QRect(800, 70, 141, 41))
        self.btn_camera.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_camera.setAutoFillBackground(False)
        self.btn_camera.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_camera.setObjectName("btn_camera")
        self.btn_myo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_myo.setGeometry(QtCore.QRect(800, 20, 141, 41))
        self.btn_myo.setAutoFillBackground(False)
        self.btn_myo.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.btn_myo.setObjectName("btn_myo")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##############Call the webcam and apply the mediapipe##########################################################

        self.webcam_apply_mediapipe = webcam_capture()

        self.webcam_apply_mediapipe.start()
        self.webcam_apply_mediapipe.ImageUpdate.connect(self.ImageUpdateSlot)

        # #初始化一个定时器
        # self.timer=QTimer()
        # self.timer.start(10000)
        # #定时器结束，触发showTime方法
        # self.timer.timeout.connect(self.slow_result_1)
        # self.timer.timeout.connect(MainWindow.close)

        self.pushButton.clicked.connect(self.slow_result_1)
        self.pushButton.clicked.connect(MainWindow.close)

    def ImageUpdateSlot(self, image):
        self.label_5.setPixmap(QPixmap.fromImage(image))

    #def CancelFeed(self):
        #self.webcam_apply_mediapipe.stop()

    ###############Open new window#########################################################
    def slow_result_1(self):
        self.webcam_apply_mediapipe.stop1()
        self.webcam_apply_mediapipe.terminate()
        self.assessmentWindow_1 = QMainWindow()
        self.ui = Ui_slow_guidance_1()
        self.ui.setupUi(self.assessmentWindow_1)
        self.assessmentWindow_1.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Test 1/3"))
        self.label.setText(_translate("MainWindow", "Press the SpaceBar to continue\n"
""))
        self.label_2.setText(_translate("MainWindow", "Slow Speed"))
        b = global_var.get_value('joint_dir')
        print(b)
        self.label_4.setText(_translate("MainWindow", "Please determine the joint location "))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.btn_camera.setText(_translate("MainWindow", "Camera feeded"))
        self.btn_myo.setText(_translate("MainWindow", "MYO Connected"))