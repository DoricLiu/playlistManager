# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Shirage_Project\YT - PlaylistAPP\workspace\Source_fix_2.0\Source_Ui\UI_About.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_AboutWindow(object):
    def setupUi(self, Ui_AboutWindow):
        Ui_AboutWindow.setObjectName("Ui_AboutWindow")
        Ui_AboutWindow.resize(323, 266)
        Ui_AboutWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Ui_AboutWindow)
        self.label.setGeometry(QtCore.QRect(20, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ui_AboutWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Ui_AboutWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Ui_AboutWindow)
        self.textEdit.setGeometry(QtCore.QRect(90, 120, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Ui_AboutWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Ui_AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_AboutWindow)

    def retranslateUi(self, Ui_AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        Ui_AboutWindow.setWindowTitle(_translate("Ui_AboutWindow", "關於本程式"))
        self.label.setText(_translate("Ui_AboutWindow", "Youtube Playlist Application"))
        self.label_2.setText(_translate("Ui_AboutWindow", "Youtube 播放清單應用程式"))
        self.label_3.setText(_translate("Ui_AboutWindow", "組員："))
        self.textEdit.setMarkdown(_translate("Ui_AboutWindow", "3A217052 劉芷君 3A217057 陳育苓\n"
"\n"
""))
        self.textEdit.setHtml(_translate("Ui_AboutWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體 Light\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:9px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3A217052 劉芷君 3A217057 陳育苓</p></body></html>"))
        self.label_4.setText(_translate("Ui_AboutWindow", "指導老師：陳瑞茂"))
