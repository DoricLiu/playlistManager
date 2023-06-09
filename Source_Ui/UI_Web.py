# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Shirage_Project\YT - PlaylistAPP\workspace\Source_fix_2.0\Source_Ui\UI_Web.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebWindow(object):
    def setupUi(self, WebWindow):
        WebWindow.setObjectName("WebWindow")
        WebWindow.resize(951, 501)
        self.wgt_center = QtWidgets.QWidget(WebWindow)
        self.wgt_center.setGeometry(QtCore.QRect(0, 0, 641, 501))
        self.wgt_center.setStyleSheet("QWidget#wgt_center{\n"
"    background:#003D79;\n"
"    border:1px solid white;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"}")
        self.wgt_center.setObjectName("wgt_center")
        self.btn_close = QtWidgets.QPushButton(self.wgt_center)
        self.btn_close.setGeometry(QtCore.QRect(590, -10, 31, 41))
        self.btn_close.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton#btn_close{color: #fe6a6d;border:none;background-color: transparent;}\n"
"\n"
"QPushButton#btn_close:hover{color:#55557f;}")
        self.btn_close.setObjectName("btn_close")
        self.btn_min = QtWidgets.QPushButton(self.wgt_center)
        self.btn_min.setGeometry(QtCore.QRect(510, -10, 31, 41))
        self.btn_min.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton#btn_min{color: #3db95a;border:none;background-color: transparent;}\n"
"\n"
"QPushButton#btn_min:hover{color:#55557f;}")
        self.btn_min.setObjectName("btn_min")
        self.btn_max = QtWidgets.QPushButton(self.wgt_center)
        self.btn_max.setGeometry(QtCore.QRect(550, -10, 31, 41))
        self.btn_max.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_max.setFont(font)
        self.btn_max.setStyleSheet("QPushButton#btn_max{color: #aaff00;border:none;background-color: transparent;}\n"
"\n"
"QPushButton#btn_max:hover{color:#55557f;}")
        self.btn_max.setObjectName("btn_max")
        self.lbl_Title = QtWidgets.QLabel(self.wgt_center)
        self.lbl_Title.setGeometry(QtCore.QRect(20, 430, 611, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Title.sizePolicy().hasHeightForWidth())
        self.lbl_Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_Title.setFont(font)
        self.lbl_Title.setStyleSheet("color: rgb(255, 255,255);\n"
"background-color: #46a3ff;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.lbl_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Title.setObjectName("lbl_Title")
        self.btn_ShowList = QtWidgets.QPushButton(self.wgt_center)
        self.btn_ShowList.setGeometry(QtCore.QRect(620, 70, 20, 91))
        self.btn_ShowList.setStyleSheet("QPushButton#btn_ShowList{\n"
"border:0px;\n"
"background-color: #46a3ff;\n"
"color: rgb(202, 202, 202);\n"
"}\n"
"\n"
"QPushButton#btn_ShowList:hover{background-color: #4d4471;}")
        self.btn_ShowList.setObjectName("btn_ShowList")
        self.wev_WebView = QtWebEngineWidgets.QWebEngineView(self.wgt_center)
        self.wev_WebView.setGeometry(QtCore.QRect(30, 30, 591, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wev_WebView.sizePolicy().hasHeightForWidth())
        self.wev_WebView.setSizePolicy(sizePolicy)
        self.wev_WebView.setProperty("url", QtCore.QUrl("about:blank"))
        self.wev_WebView.setObjectName("wev_WebView")
        self.wgt_right = QtWidgets.QWidget(WebWindow)
        self.wgt_right.setGeometry(QtCore.QRect(640, 0, 311, 501))
        self.wgt_right.setStyleSheet("QWidget#wgt_right{\n"
"    background:gray;\n"
"    border:1px solid white;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"")
        self.wgt_right.setObjectName("wgt_right")
        self.lsw_VideoList = QtWidgets.QListWidget(self.wgt_right)
        self.lsw_VideoList.setGeometry(QtCore.QRect(10, 10, 251, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lsw_VideoList.sizePolicy().hasHeightForWidth())
        self.lsw_VideoList.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lsw_VideoList.setFont(font)
        self.lsw_VideoList.setStyleSheet("QListWidget#lsw_VideoList{\n"
"    background:#ffffff;\n"
"    border:1px solid white;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"}")
        self.lsw_VideoList.setObjectName("lsw_VideoList")
        self.btn_Pre = QtWidgets.QPushButton(self.wgt_right)
        self.btn_Pre.setGeometry(QtCore.QRect(270, 10, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Pre.sizePolicy().hasHeightForWidth())
        self.btn_Pre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_Pre.setFont(font)
        self.btn_Pre.setStyleSheet("QPushButton#btn_Pre{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton#btn_Pre:hover{\n"
"background-color: #4d4471;\n"
"color:#FFFFFF;\n"
"}")
        self.btn_Pre.setObjectName("btn_Pre")
        self.btn_Next = QtWidgets.QPushButton(self.wgt_right)
        self.btn_Next.setGeometry(QtCore.QRect(270, 50, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Next.sizePolicy().hasHeightForWidth())
        self.btn_Next.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_Next.setFont(font)
        self.btn_Next.setStyleSheet("QPushButton#btn_Next{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton#btn_Next:hover{\n"
"background-color: #4d4471;\n"
"color:#FFFFFF;\n"
"}")
        self.btn_Next.setObjectName("btn_Next")
        self.btn_Sequential = QtWidgets.QPushButton(self.wgt_right)
        self.btn_Sequential.setGeometry(QtCore.QRect(270, 90, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Sequential.sizePolicy().hasHeightForWidth())
        self.btn_Sequential.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.btn_Sequential.setFont(font)
        self.btn_Sequential.setStyleSheet("QPushButton#btn_Sequential{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton#btn_Sequential:hover{\n"
"background-color: #4d4471;\n"
"color:#FFFFFF;\n"
"}")
        self.btn_Sequential.setObjectName("btn_Sequential")

        self.retranslateUi(WebWindow)
        QtCore.QMetaObject.connectSlotsByName(WebWindow)

    def retranslateUi(self, WebWindow):
        _translate = QtCore.QCoreApplication.translate
        WebWindow.setWindowTitle(_translate("WebWindow", "Youtube嵌入式播放器"))
        self.btn_close.setText(_translate("WebWindow", "▬"))
        self.btn_min.setText(_translate("WebWindow", "▬"))
        self.btn_max.setText(_translate("WebWindow", "▬"))
        self.lbl_Title.setText(_translate("WebWindow", "無"))
        self.btn_ShowList.setText(_translate("WebWindow", "◂"))
        self.btn_Pre.setText(_translate("WebWindow", "▲"))
        self.btn_Next.setText(_translate("WebWindow", "▼"))
        self.btn_Sequential.setText(_translate("WebWindow", "↻"))
from PyQt5 import QtWebEngineWidgets
