# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_button.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, QtWidget):
        QtWidget.setObjectName("Form")
        QtWidget.resize(142, 42)
        self.stopbutton = QtWidgets.QPushButton(Form)
        self.stopbutton.setGeometry(QtCore.QRect(96, 0, 44, 40))
        self.stopbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopbutton.setIcon(icon)
        self.stopbutton.setIconSize(QtCore.QSize(32, 32))
        self.stopbutton.setObjectName("stopbutton")
        self.startbutton = QtWidgets.QPushButton(Form)
        self.startbutton.setGeometry(QtCore.QRect(0, 0, 44, 40))
        self.startbutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icon_start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startbutton.setIcon(icon1)
        self.startbutton.setIconSize(QtCore.QSize(32, 32))
        self.startbutton.setObjectName("startbutton")
        self.pausebutton = QtWidgets.QPushButton(Form)
        self.pausebutton.setGeometry(QtCore.QRect(49, 0, 44, 40))
        self.pausebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pausebutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/icon_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausebutton.setIcon(icon2)
        self.pausebutton.setIconSize(QtCore.QSize(32, 32))
        self.pausebutton.setObjectName("pausebutton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, QtWidget):
        _translate = QtCore.QCoreApplication.translate