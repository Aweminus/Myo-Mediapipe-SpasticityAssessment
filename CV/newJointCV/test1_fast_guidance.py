from PyQt5 import QtCore, QtGui, QtWidgets
from test1_fast_input import Ui_fast_input_1
from webcam_mediapipe import *
from webcam_mediapipe_right import *
import global_var
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QTimer,QDateTime
import sys
import time

class Ui_fast_guidance_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 80, 500, 41))
        self.label_3.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(125, 520, 750, 21))
        self.label.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(125, 20, 750, 61))
        self.label_2.setStyleSheet("font: 75 28pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(825, 500, 81, 31))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
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


        self.wgt_player = QVideoWidget(self.centralwidget)
        self.wgt_player.setGeometry(QtCore.QRect(125, 125, 750, 350))
        self.wgt_player.setObjectName("wgt_player")

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(r'C:\Users\pzhan\Desktop\Myo-CV-Spasticity-Assessment\newJointCV\test_video.mp4')))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player=QMediaPlayer()
        self.player.setVideoOutput(self.wgt_player)
        self.player.setPlaylist(self.playlist)
        self.player.play()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.slow_result_1)
        self.pushButton.clicked.connect(MainWindow.close)

    def ImageUpdateSlot(self, image):
        self.label_5.setPixmap(QPixmap.fromImage(image))

    ###############The function of new window#########################################################
    def slow_result_1(self):
        self.assessmentWindow_1 = QMainWindow()
        self.ui = Ui_fast_input_1()
        self.ui.setupUi(self.assessmentWindow_1)
        self.assessmentWindow_1.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Press the SpaceBar to start the assessment"))
        self.label_3.setText(_translate("MainWindow", "Move at 340°/s"))
        self.label_2.setText(_translate("MainWindow", "Fast Speed Guidance"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.btn_camera.setText(_translate("MainWindow", "Camera feeded"))
        self.btn_myo.setText(_translate("MainWindow", "MYO Connected"))
