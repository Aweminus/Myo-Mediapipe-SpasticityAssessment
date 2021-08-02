# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_mediuminput.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
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
        self.label.setGeometry(QtCore.QRect(250, 530, 500, 21))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Test 1/3"))
        self.label.setText(_translate("MainWindow", "When finished click the SpaceBar"))
        self.label_2.setText(_translate("MainWindow", "Medium Speed"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.btn_camera.setText(_translate("MainWindow", "Camera feeded"))
        self.btn_myo.setText(_translate("MainWindow", "MYO Connected"))

if __name__ == '__main__':

 QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
 app = QApplication(sys.argv)
 #ui_ready4assessment = ready4assessment()
 #ui_3 = slow_input_1()
 myMainWindow = QMainWindow()
 myUi = Ui_MainWindow()
 myUi.setupUi(myMainWindow)
 myMainWindow.show()
sys.exit(app.exec_())