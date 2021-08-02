from PyQt5 import QtCore, QtGui, QtWidgets
from test2_slow_result import Ui_slow_result_2
from webcam_mediapipe import *
from webcam_mediapipe_right import *
import global_var

class Ui_slow_input_2(object):
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
        self.label.setGeometry(QtCore.QRect(125, 485, 750, 41))
        self.label.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 500, 61))
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(125, 125, 750, 350))
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(125, 535, 750, 31))
        self.label_6.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
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

        ##############Call the webcam and apply the mediapipe##########################################################
        joint_dir = global_var.get_value('joint_dir')
        if (joint_dir == 0):
            self.webcam_apply_mediapipe = webcam_apply_mediapipe()
        else:
            self.webcam_apply_mediapipe = webcam_apply_mediapipe_right()

        self.webcam_apply_mediapipe.terminate()

        self.webcam_apply_mediapipe.start()
        self.webcam_apply_mediapipe.ImageUpdate.connect(self.ImageUpdateSlot)

        self.timer = QTimer()
        #print(self.timer)
        self.timer.start(global_var.get_value('input_time'))

        self.timer.timeout.connect(self.slow_result_1)
        self.timer.timeout.connect(MainWindow.close)

        self.pushButton.clicked.connect(self.restart)
        self.pushButton.clicked.connect(MainWindow.close)

        self.countdown = global_var.get_value('input_time') // 1000
        self.time = QTimer()
        #print(self.time)
        self.time.start(1000)
        self.time.timeout.connect(self.Refresh)

    def ImageUpdateSlot(self, image):
        self.label_5.setPixmap(QPixmap.fromImage(image))

    # def CancelFeed(self):
    # self.webcam_apply_mediapipe.stop()
    ###############Open new window#########################################################
    def slow_result_1(self):
        self.timer.stop()
        self.time.stop()
        self.webcam_apply_mediapipe.stop1()
        self.webcam_apply_mediapipe.terminate()
        self.assessmentWindow_1 = QMainWindow()
        self.ui = Ui_slow_result_2()
        self.ui.setupUi(self.assessmentWindow_1)
        self.assessmentWindow_1.show()

    def restart(self):
        self.timer.stop()
        self.time.stop()
        self.webcam_apply_mediapipe.stop2()
        self.webcam_apply_mediapipe.terminate()
        self.assessmentWindow_1 = QMainWindow()
        self.ui = Ui_slow_input_2()
        self.ui.setupUi(self.assessmentWindow_1)
        self.assessmentWindow_1.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_2.setText(_translate("MainWindow", "Slow Speed"))
        self.label_3.setText(_translate("MainWindow", "Test 2/3"))
        # self.label.setText(_translate("Assessment Ongoing:" + str(self.countdown) + "seconds remaining..."))
        x = global_var.get_value('input_time')
        self.label.setText(_translate("MainWindow", "Assessment Ongoing: " + str(x // 1000) + " seconds remaining..."))
        self.label_6.setText(_translate("MainWindow", "Press Spacebar to restart"))
        self.pushButton.setText(_translate("MainWindow", "Restart"))
        self.btn_myo.setText(_translate("MainWindow", "MYO Connected"))
        self.btn_camera.setText(_translate("MainWindow", "Camera feeded"))

    def Refresh(self):
        _translate = QtCore.QCoreApplication.translate
        self.countdown -= 1
        self.label.setText(
            _translate("MainWindow", "Assessment Ongoing: " + str(self.countdown) + " seconds remaining..."))