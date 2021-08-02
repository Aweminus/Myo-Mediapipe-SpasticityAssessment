# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do nñot edit this file unless you know what you are doing.


import sys

import keyboard
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow

from ready4assessment import Ui_ready4assessment
from test1_slow_input import *
import sqlite3
import global_var

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(500, 300))
        self.label.setMaximumSize(QtCore.QSize(500, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/login_background.png"))
        self.label.setObjectName("label")
        self.edt_patientname = QtWidgets.QLineEdit(Form)
        self.edt_patientname.setGeometry(QtCore.QRect(170, 120, 151, 31))
        self.edt_patientname.setStyleSheet("background-color: rgb(150, 150, 150);\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.edt_patientname.setObjectName("edt_patientname")
        self.edt_password = QtWidgets.QLineEdit(Form)
        self.edt_password.setGeometry(QtCore.QRect(170, 160, 151, 31))
        self.edt_password.setStyleSheet("background-color: rgb(150, 150, 150);\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.edt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edt_password.setObjectName("edt_password")
        self.btn_login = QtWidgets.QPushButton(Form)
        self.btn_login.setGeometry(QtCore.QRect(340, 130, 61, 51))
        self.btn_login.setStyleSheet("background-color: rgb(85, 170, 0);\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.btn_login.setAutoRepeat(False)
        self.btn_login.setAutoExclusive(False)
        self.btn_login.setAutoDefault(False)
        self.btn_login.setObjectName("btn_login")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 200, 331, 31))
        self.label_2.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btn_login.clicked.connect(self.readyassessment)
        self.edt_password.returnPressed.connect(self.readyassessment)

        #if self.readyassessment is True:
        #    Form.close()
        #    print("true")
        #self.btn_login.clicked.connect(Form.close)

    #     if keyboard.is_pressed('a'):
    #         self.test_method()
    #
    # def test_method(self):
    #     print('Space key pressed')



    #def keyPressEvent(self,event):
    #    print(event.key())
    #    if event.key() == Qt.Key_Return:
    #        press("enter")
    #        self.btn_login.clicked.connect(self.readyassessment)
    #        self.readyassessment()


    def readyassessment(self):
        username = self.edt_patientname.text()
        password = self.edt_password.text()

        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username,password))
        if(len(result.fetchall())>0):
            print("User Found !")
            self.close()
            self.readyWindow = QMainWindow()
            self.ui = Ui_ready4assessment()
            self.ui.setupUi(self.readyWindow)
            self.readyWindow.show()
        else:
            print("User Not Found !")


        print("login")
        #ui_ready4assessment.show()
        #Ui_Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.edt_patientname.setPlaceholderText(_translate("Form", "Patient Name"))
        self.edt_password.setPlaceholderText(_translate("Form", "Password"))
        self.btn_login.setText(_translate("Form", "OK"))
        self.label_2.setText(_translate("Form", "Only clickable when myo and camera are connected."))


if __name__ == '__main__':
 global_var._init()
 QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
 app = QApplication(sys.argv)
 #ui_ready4assessment = ready4assessment()
 #ui_3 = slow_input_1()
 myMainWindow = QMainWindow()
 myUi = Ui_Form()
 myUi.setupUi(myMainWindow)
 myMainWindow.show()
sys.exit(app.exec_())

