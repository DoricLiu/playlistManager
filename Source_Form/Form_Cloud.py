import sys
sys.path.append('..')

import Source_Ui.UI_Cloud as UI_Cloud
from PyQt5 import QtCore, QtGui, QtWidgets


class Form_Cloud(UI_Cloud.Ui_CloudWindow):
    __form_Cloud = None
    __acpResault = False
    listPrivacy = "private"

    def setupUi(self, form_Cloud):
        super().setupUi(form_Cloud)
        self.__form_Cloud = form_Cloud
        self.__form_Cloud.setWindowOpacity(1)
        self.__form_Cloud.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.__form_Cloud.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.__form_Cloud.setFixedSize(self.__form_Cloud.size())
        self.__acpResault = False
        form_Cloud.setWindowIcon(QtGui.QIcon('img/icon/icon_Cloud.ico'))
        self.radioButton_private.setChecked(True)
        self.__setEventHandle(form_Cloud)

    def __setEventHandle(self, form_Cloud):
        self.btn_close.clicked.connect(self.__btn_close__Clicked)
        self.btn_Resault_AddNewList.clicked.connect(self.__btn_Resault_AddNewList_Clicked)
        self.btn_Resault_API.clicked.connect(self.__btn_Resault_Clicked)
        self.btn_Resault_DeleteList.clicked.connect(self.__btn_Resault_Clicked)

        self.radioButton_private.clicked.connect(self.__radioButton_Clicked)
        self.radioButton_public.clicked.connect(self.__radioButton_Clicked)
        self.radioButton_unlisted.clicked.connect(self.__radioButton_Clicked)

    def __btn_close__Clicked(self):
        self.__form_Cloud.close()

    # Event:確認執行
    def __btn_Resault_Clicked(self):
        self.__acpResault = True
        self.__form_Cloud.close()

    # Event:送出建立播放清單所需的資料
    def __btn_Resault_AddNewList_Clicked(self):
        if self.txt_NewList_Title.text() and self.txt_NewList_Title.text() != ' ':
            self.__acpResault = True
            self.__form_Cloud.close()
        else:
            QtWidgets.QMessageBox.critical(self.__form_Cloud, '錯誤訊息', '清單名稱不可為空白或留空.')
            return

    # Event:更改隱私設定狀態
    def __radioButton_Clicked(self):
        if self.radioButton_private.isChecked():
            self.listPrivacy = "private"
            self.radioButton_public.setChecked(False)
            self.radioButton_unlisted.setChecked(False)
        
        elif self.radioButton_unlisted.isChecked():
            self.listPrivacy = "unlisted"
            self.radioButton_public.setChecked(False)
            self.radioButton_private.setChecked(False)
        
        else:
            self.listPrivacy = "public"
            self.radioButton_private.setChecked(False)
            self.radioButton_unlisted.setChecked(False)

    # Func:回傳使用者確定or取消
    def getAcceptResault(self):
        return self.__acpResault
