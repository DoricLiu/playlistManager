# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Shirage_Project\YT - PlaylistAPP\workspace\Source_fix_2.0\Source_Ui\UI_VideoInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoWindows(object):
    def setupUi(self, InfoWindows):
        InfoWindows.setObjectName("InfoWindows")
        InfoWindows.resize(312, 371)
        self.wgt_center = QtWidgets.QWidget(InfoWindows)
        self.wgt_center.setGeometry(QtCore.QRect(0, 0, 311, 371))
        self.wgt_center.setStyleSheet("QWidget#wgt_center{\n"
"    background:gray;\n"
"    border:1px solid white;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"}")
        self.wgt_center.setObjectName("wgt_center")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.wgt_center)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 271, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_Title = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Title.sizePolicy().hasHeightForWidth())
        self.lbl_Title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_Title.setFont(font)
        self.lbl_Title.setAcceptDrops(True)
        self.lbl_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Title.setObjectName("lbl_Title")
        self.verticalLayout_2.addWidget(self.lbl_Title)
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("border:none;\n"
"background-color: gray;")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.lbl_UploadDate = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_UploadDate.sizePolicy().hasHeightForWidth())
        self.lbl_UploadDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lbl_UploadDate.setFont(font)
        self.lbl_UploadDate.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_UploadDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_UploadDate.setObjectName("lbl_UploadDate")
        self.gridLayout.addWidget(self.lbl_UploadDate, 2, 1, 1, 1)
        self.lbl_Views = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Views.sizePolicy().hasHeightForWidth())
        self.lbl_Views.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lbl_Views.setFont(font)
        self.lbl_Views.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Views.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Views.setObjectName("lbl_Views")
        self.gridLayout.addWidget(self.lbl_Views, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lbl_Autor = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Autor.sizePolicy().hasHeightForWidth())
        self.lbl_Autor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lbl_Autor.setFont(font)
        self.lbl_Autor.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Autor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Autor.setObjectName("lbl_Autor")
        self.gridLayout.addWidget(self.lbl_Autor, 1, 1, 1, 1)
        self.lbl_Rate = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Rate.sizePolicy().hasHeightForWidth())
        self.lbl_Rate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.lbl_Rate.setFont(font)
        self.lbl_Rate.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Rate.setObjectName("lbl_Rate")
        self.gridLayout.addWidget(self.lbl_Rate, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.btn_close = QtWidgets.QPushButton(self.wgt_center)
        self.btn_close.setGeometry(QtCore.QRect(284, 0, 20, 31))
        self.btn_close.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton#btn_close{color: #FFFFFF;border:none;background-color: transparent;}\n"
"\n"
"QPushButton#btn_close:hover{color:#55557f;}")
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(InfoWindows)
        QtCore.QMetaObject.connectSlotsByName(InfoWindows)

    def retranslateUi(self, InfoWindows):
        _translate = QtCore.QCoreApplication.translate
        InfoWindows.setWindowTitle(_translate("InfoWindows", "Dialog"))
        self.lbl_Title.setText(_translate("InfoWindows", "TextLabel"))
        self.label_1.setText(_translate("InfoWindows", " 上傳日期："))
        self.label.setText(_translate("InfoWindows", " 評價："))
        self.lbl_UploadDate.setText(_translate("InfoWindows", "TextLabel"))
        self.lbl_Views.setText(_translate("InfoWindows", "TextLabel"))
        self.label_3.setText(_translate("InfoWindows", " 瀏覽次數："))
        self.lbl_Autor.setText(_translate("InfoWindows", "TextLabel"))
        self.lbl_Rate.setText(_translate("InfoWindows", "TextLabel"))
        self.label_2.setText(_translate("InfoWindows", " 影片作者："))
        self.btn_close.setText(_translate("InfoWindows", "✖"))