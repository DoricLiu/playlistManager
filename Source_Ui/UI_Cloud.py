# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Shirage_Project\YT - PlaylistAPP\workspace\Test_file_archive\UI_Cloud.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CloudWindow(object):
    def setupUi(self, CloudWindow):
        CloudWindow.setObjectName("CloudWindow")
        CloudWindow.resize(392, 281)
        self.wgt_Center = QtWidgets.QWidget(CloudWindow)
        self.wgt_Center.setGeometry(QtCore.QRect(0, 0, 391, 281))
        self.wgt_Center.setStyleSheet("QWidget#wgt_Center{\n"
"background-color: #acacac;\n"
"border:5px solid #515151;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}")
        self.wgt_Center.setObjectName("wgt_Center")
        self.btn_close = QtWidgets.QPushButton(self.wgt_Center)
        self.btn_close.setGeometry(QtCore.QRect(350, 10, 20, 31))
        self.btn_close.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("QPushButton#btn_close{color: #FFFFFF;border:none;background-color: transparent;}\n"
"\n"
"QPushButton#btn_close:hover{color:#55557f;}")
        self.btn_close.setObjectName("btn_close")
        self.btn_Resault_API = QtWidgets.QPushButton(self.wgt_Center)
        self.btn_Resault_API.setGeometry(QtCore.QRect(280, 50, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Resault_API.setFont(font)
        self.btn_Resault_API.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 113, 113);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;")
        self.btn_Resault_API.setObjectName("btn_Resault_API")
        self.lbl_Text = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text.setGeometry(QtCore.QRect(20, 10, 96, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Text.setFont(font)
        self.lbl_Text.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text.setObjectName("lbl_Text")
        self.txt_API_key = QtWidgets.QLineEdit(self.wgt_Center)
        self.txt_API_key.setGeometry(QtCore.QRect(20, 40, 251, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_API_key.setFont(font)
        self.txt_API_key.setStyleSheet("border:3px solid white;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.txt_API_key.setObjectName("txt_API_key")
        self.lbl_Text_2 = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text_2.setGeometry(QtCore.QRect(20, 70, 171, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Text_2.setFont(font)
        self.lbl_Text_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text_2.setObjectName("lbl_Text_2")
        self.txt_delete_target = QtWidgets.QLineEdit(self.wgt_Center)
        self.txt_delete_target.setGeometry(QtCore.QRect(20, 100, 251, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_delete_target.setFont(font)
        self.txt_delete_target.setStyleSheet("border:3px solid white;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.txt_delete_target.setObjectName("txt_delete_target")
        self.btn_Resault_DeleteList = QtWidgets.QPushButton(self.wgt_Center)
        self.btn_Resault_DeleteList.setGeometry(QtCore.QRect(280, 100, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Resault_DeleteList.setFont(font)
        self.btn_Resault_DeleteList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 113, 113);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;")
        self.btn_Resault_DeleteList.setObjectName("btn_Resault_DeleteList")
        self.lbl_Text_3 = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text_3.setGeometry(QtCore.QRect(10, 130, 361, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Text_3.setFont(font)
        self.lbl_Text_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text_3.setObjectName("lbl_Text_3")
        self.txt_NewList_Title = QtWidgets.QLineEdit(self.wgt_Center)
        self.txt_NewList_Title.setGeometry(QtCore.QRect(70, 160, 291, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_NewList_Title.setFont(font)
        self.txt_NewList_Title.setStyleSheet("border:3px solid white;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.txt_NewList_Title.setObjectName("txt_NewList_Title")
        self.lbl_Text_4 = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text_4.setGeometry(QtCore.QRect(20, 200, 51, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Text_4.setFont(font)
        self.lbl_Text_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text_4.setObjectName("lbl_Text_4")
        self.lbl_Text_5 = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text_5.setGeometry(QtCore.QRect(20, 160, 61, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_Text_5.setFont(font)
        self.lbl_Text_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text_5.setObjectName("lbl_Text_5")
        self.txt_NewList_Descript = QtWidgets.QLineEdit(self.wgt_Center)
        self.txt_NewList_Descript.setGeometry(QtCore.QRect(70, 200, 291, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.txt_NewList_Descript.setFont(font)
        self.txt_NewList_Descript.setStyleSheet("border:3px solid white;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.txt_NewList_Descript.setObjectName("txt_NewList_Descript")
        self.lbl_Text_6 = QtWidgets.QLabel(self.wgt_Center)
        self.lbl_Text_6.setGeometry(QtCore.QRect(20, 240, 61, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lbl_Text_6.setFont(font)
        self.lbl_Text_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_Text_6.setObjectName("lbl_Text_6")
        self.radioButton_private = QtWidgets.QRadioButton(self.wgt_Center)
        self.radioButton_private.setGeometry(QtCore.QRect(90, 239, 61, 31))
        self.radioButton_private.setObjectName("radioButton_private")
        self.radioButton_public = QtWidgets.QRadioButton(self.wgt_Center)
        self.radioButton_public.setGeometry(QtCore.QRect(240, 240, 61, 31))
        self.radioButton_public.setObjectName("radioButton_public")
        self.radioButton_unlisted = QtWidgets.QRadioButton(self.wgt_Center)
        self.radioButton_unlisted.setGeometry(QtCore.QRect(160, 240, 61, 31))
        self.radioButton_unlisted.setObjectName("radioButton_unlisted")
        self.btn_Resault_AddNewList = QtWidgets.QPushButton(self.wgt_Center)
        self.btn_Resault_AddNewList.setGeometry(QtCore.QRect(300, 240, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Resault_AddNewList.setFont(font)
        self.btn_Resault_AddNewList.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(113, 113, 113);\n"
"    border:none;\n"
"    padding: 3px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;")
        self.btn_Resault_AddNewList.setObjectName("btn_Resault_AddNewList")

        self.retranslateUi(CloudWindow)
        QtCore.QMetaObject.connectSlotsByName(CloudWindow)

    def retranslateUi(self, CloudWindow):
        _translate = QtCore.QCoreApplication.translate
        CloudWindow.setWindowTitle(_translate("CloudWindow", "雲端設定"))
        self.btn_close.setText(_translate("CloudWindow", "✖"))
        self.btn_Resault_API.setText(_translate("CloudWindow", "確認"))
        self.lbl_Text.setText(_translate("CloudWindow", "API Key："))
        self.lbl_Text_2.setText(_translate("CloudWindow", "欲刪除之清單網址或ID："))
        self.btn_Resault_DeleteList.setText(_translate("CloudWindow", "確認"))
        self.lbl_Text_3.setText(_translate("CloudWindow", "＝＝＝建立新清單＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝"))
        self.lbl_Text_4.setText(_translate("CloudWindow", "敘述："))
        self.lbl_Text_5.setText(_translate("CloudWindow", "名稱："))
        self.lbl_Text_6.setText(_translate("CloudWindow", "隱私設定"))
        self.radioButton_private.setText(_translate("CloudWindow", "私人"))
        self.radioButton_public.setText(_translate("CloudWindow", "公開"))
        self.radioButton_unlisted.setText(_translate("CloudWindow", "不公開"))
        self.btn_Resault_AddNewList.setText(_translate("CloudWindow", "確認"))
