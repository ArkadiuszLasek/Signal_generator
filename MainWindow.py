# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plot.setGeometry(QtCore.QRect(180, 120, 93, 28))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.lineEdit_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time.setGeometry(QtCore.QRect(260, 40, 41, 22))
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(30, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.doubleSpinBox_time = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_time.setGeometry(QtCore.QRect(180, 40, 62, 22))
        self.doubleSpinBox_time.setObjectName("doubleSpinBox_time")
        self.lineEdit_amp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_amp.setGeometry(QtCore.QRect(260, 70, 41, 22))
        self.lineEdit_amp.setObjectName("lineEdit_amp")
        self.label_amp = QtWidgets.QLabel(self.centralwidget)
        self.label_amp.setGeometry(QtCore.QRect(30, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_amp.setFont(font)
        self.label_amp.setObjectName("label_amp")
        self.doubleSpinBox_amp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_amp.setGeometry(QtCore.QRect(180, 70, 62, 22))
        self.doubleSpinBox_amp.setObjectName("doubleSpinBox_amp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 21))
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
        self.pushButton_plot.setText(_translate("MainWindow", "Plot"))
        self.lineEdit_time.setText(_translate("MainWindow", "10.0"))
        self.label_time.setText(_translate("MainWindow", "Time [s]"))
        self.lineEdit_amp.setText(_translate("MainWindow", "1.0"))
        self.label_amp.setText(_translate("MainWindow", "Amplitude [mm]"))

