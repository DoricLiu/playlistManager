import sys
sys.path.append('..')

import threading
import json
import random
import google.oauth2.credentials as GO2_credentials
import google.auth.transport.requests as GAT_requests

import Source_Other.ThreadHandle as trd_Handle
import Source_Other.DialogClass as DialogClass
import Source_Other.SQLClass as SQLClass
import Source_Other.FileClass as FileClass
import Source_Other.UserHandle as UserHandle
import Source_Video.VideoHandle as vh_Handle
import Source_Video.VideoClass as VideoClass

import Form_Web as form_Web
import Source_Form.Form_About as form_About
import Source_Form.Form_Cloud as form_Cloud
import Source_Form.Form_VideoList as form_VideoList
import Source_Form.Form_VideoInfo as form_VideoInfo
import Source_Ui.UI_Main as UI_Main

from PyQt5 import QtGui, QtWidgets, QtCore


class Form_Main(UI_Main.Ui_MainWindow):
    with open("Source_Other/setting.json", "r") as settingfile:
        __setting=json.load(settingfile)
    with open("Source_Other/credentialsFile.json", "r") as credentialfile:
        __credential=json.load(credentialfile)
    i_PlayList = {}
    i_ListName = None
    __clipboard = []
    __cliptmp = {}
    __thisWindow = None
    __str_WindowsTitle = '播放清單'
    trd_VideoList = None

    def setupUi(self, form_Main):
        super().setupUi(form_Main)
        self.__thisWindow = form_Main
        form_Main.setFixedSize(form_Main.size())
        form_Main.setWindowTitle('Youtube 播放工具')
        form_Main.setWindowOpacity(1.0)
        form_Main.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        form_Main.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        form_Main.setWindowIcon(QtGui.QIcon('img/icon/icon_Main.ico'))
        self.btn_SequentialPlayVideo.setText('播\n放\n影\n片')
        self.cbb_HotVideoCategories.setStyleSheet("""
            QComboBox::down-arrow {width:15px;image: url(./img/icon/appbar.chevron.down2.png);}
            QComboBox::down-arrow:on {width:15px;image: url(./img/icon/appbar.chevron.down.png);}
            QComboBox{color: rgb(50, 50, 75);background-color: rgb(236, 236, 236);border-top-left-radius:10px;border-bottom-left-radius:10px;border-top-right-radius:10px;border-bottom-right-radius:10px;}
            QComboBox::drop-down:button{border-top-right-radius:10px;border-bottom-right-radius:10px;background-color: rgb(170, 170, 255);}
        """)
        self.lsw_VideoList.horizontalScrollBar().setStyleSheet("""
            QScrollBar:horizontal {height: 8px;background: #DDD;}
            QScrollBar::handle:horizontal {background: #AAA;}
            QScrollBar::handle:horizontal:hover {background: #888;}
            QScrollBar::sub-line:horizontal, QScrollBar::add-line:horizontal {width: 0;height: 0;}
            """)
        self.lsw_VideoList.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {width: 8px;background: #DDD;padding-bottom: 8px;}
            QScrollBar::handle:vertical {background: #AAA;}
            QScrollBar::handle:vertical:hover {background: #888;}
            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {width: 0;height: 0;}
            """)
        self.btn_max.setEnabled(False)
        self.wgt_Tools.setVisible(False)
        self.menubar.setStyleSheet('height:0px;')
        self.lbl_FileName.setText(self.__str_WindowsTitle + '［］')
        self.trd_VideoList = threading.Thread(target=self.__getVideoThread)
        self.__checkBoxStateSetup()
        self.txt_VideoUrl.setLineWrapMode(self.txt_VideoUrl.WidgetWidth)
        self.txt_VideoUrl.setText(
            '請輸入清單網址，多筆影片請輸入ID，並用,間隔，一次最多50筆。')
        self.__setEventHandle(form_Main)
        self.__setCountryName()

    def __setEventHandle(self, form_Main):
        self.btn_GetHotViedoList.clicked.connect(
            self.btn_GetHotViedoList_Click)
        self.checkBox_AutoSelectVideo.clicked.connect(
            self.__checkboxsStateChanged)
        self.checkBox_RandomAddingVideo.clicked.connect(
            self.__checkboxsStateChanged)
        self.btn_AddVideoUrl.clicked.connect(self.__btn_AddVideoUrl_Click)
        self.btn_AddVideoListUrl.clicked.connect(
            self.__btn_AddVideoListUrl_Click)
        self.lsw_VideoList.doubleClicked.connect(
            self.__lsw_VideoList_DoubleClick)
        self.btn_SequentialPlayVideo.clicked.connect(
            self.__btn_SequentialPlayVideo_Click)
        self.btn_close.clicked.connect(self.__btn_close_Clicked)
        self.btn_min.clicked.connect(self.__btn_min_Clicked)
        self.hs_Opacity.valueChanged.connect(self.__hs_Opacity_ValueChanged)

        self.act_NewFile.triggered.connect(self.__act_NewFile_Triggered)
        self.act_ReadFile.triggered.connect(self.__act_ReadFile_Triggered)
        self.act_SaveFile.triggered.connect(self.__act_SaveFile_Triggered)
        self.act_SaveNewFile.triggered.connect(
            self.__act_SaveNewFile_Triggered)
        self.act_CloseForm.triggered.connect(self.__act_CloseForm_Triggered)

        self.act_Cut.triggered.connect(self.__act_Cut_Triggered)
        self.act_Copy.triggered.connect(self.__act_Copy_Triggered)
        self.act_Paste.triggered.connect(self.__act_Paste_Triggered)
        self.act_Delete.triggered.connect(self.__act_Delete_Triggered)
        self.act_SelectAll.triggered.connect(self.__act_SelectAll_Triggered)

        self.menu_CloudHandle.aboutToShow.connect(
            self.__menu_CloudHandle_Triggered)
        self.act_Connect.triggered.connect(self.__act_login)
        self.act_CreateNewListOnYoutube.triggered.connect(self.__act_CreateNewListOnYoutube_Triggered)
        self.act_DeleteSpecificList.triggered.connect(self.__act_DeleteSpecificList_Triggered)
        self.act_InputAPIkey.triggered.connect(
            self.__act_InputAPIkey_Triggered)

        self.act_Txt.triggered.connect(self.__act_Txt_Triggered)
        self.act_Excel.triggered.connect(self.__act_Excel_Triggered)

        self.act_About.triggered.connect(self.__act_About_Triggered)
        self.btn_WgtClose.clicked.connect(self.__btn_WgtClose_Clicked)
        self.btn_File.clicked.connect(self.__btn_File_Clicked)
        self.btn_Edit.clicked.connect(self.__btn_Edit_Clicked)
        self.btn_cloud.clicked.connect(self.__btn_cloud_Clicked)
        self.btn_Create.clicked.connect(self.__btn_Create_Clicked)
        self.btn_About.clicked.connect(self.__btn_About_Clicked)

    def __hs_Opacity_ValueChanged(self):
        self.__thisWindow.setWindowOpacity(self.hs_Opacity.value() / 10)

    def __btn_File_Clicked(self):
        self.__btn_XXXX_Disconnect()
        self.wgt_Tools.setVisible(True)
        self.btn_Act1.setText('新建清單 (Ctl+N)')
        self.btn_Act1.clicked.connect(self.__act_NewFile_Triggered)
        self.btn_Act2.setText('開啟清單 (Ctl+O)')
        self.btn_Act2.clicked.connect(self.__act_ReadFile_Triggered)
        self.btn_Act3.setText('儲存清單 (Ctl+S)')
        self.btn_Act3.clicked.connect(self.__act_SaveFile_Triggered)
        self.btn_Act4.setText('另存清單')
        self.btn_Act4.clicked.connect(self.__act_SaveNewFile_Triggered)
        self.btn_Act5.setText('關閉 (Esc)')
        self.btn_Act5.clicked.connect(self.__act_CloseForm_Triggered)

    def __btn_Edit_Clicked(self):
        self.__btn_XXXX_Disconnect()
        self.wgt_Tools.setVisible(True)
        self.btn_Act1.setText('剪下 (Ctl+X)')
        self.btn_Act1.clicked.connect(self.__act_Cut_Triggered)
        self.btn_Act2.setText('複製 (Ctl+C)')
        self.btn_Act2.clicked.connect(self.__act_Copy_Triggered)
        self.btn_Act3.setText('貼上 (Ctl+V)')
        self.btn_Act3.clicked.connect(self.__act_Paste_Triggered)
        self.btn_Act4.setText('刪除 (Del)')
        self.btn_Act4.clicked.connect(self.__act_Delete_Triggered)
        self.btn_Act5.setText('全部選取 (Ctl+A)')
        self.btn_Act5.clicked.connect(self.__act_SelectAll_Triggered)

    def __btn_cloud_Clicked(self):
        self.__btn_XXXX_Disconnect()
        self.wgt_Tools.setVisible(True)
        self.btn_Act1.setText('登入帳號 (=)')
        self.btn_Act1.clicked.connect(self.__act_login)
        self.btn_Act2.setText('建立新的清單 (F1)')
        self.btn_Act2.clicked.connect(self.__act_CreateNewListOnYoutube_Triggered)
        self.btn_Act3.setText('刪除指定清單 (F2)')
        self.btn_Act3.clicked.connect(self.__act_DeleteSpecificList_Triggered)
        self.btn_Act4.setText('輸入API Key')
        self.btn_Act4.clicked.connect(self.__act_InputAPIkey_Triggered)
        self.btn_Act5.setText('')
        self.btn_Act5.clicked.connect(self.__btn_XXXX_Pass)

    def __btn_Create_Clicked(self):
        self.__btn_XXXX_Disconnect()
        self.wgt_Tools.setVisible(True)
        self.btn_Act1.setText('導出文本 (Ctl+F1)')
        self.btn_Act1.clicked.connect(self.__act_Txt_Triggered)
        self.btn_Act2.setText('導出活頁簿 (Ctl+F2)')
        self.btn_Act2.clicked.connect(self.__act_Excel_Triggered)
        self.btn_Act3.setText('')
        self.btn_Act3.clicked.connect(self.__btn_XXXX_Pass)
        self.btn_Act4.setText('')
        self.btn_Act4.clicked.connect(self.__btn_XXXX_Pass)
        self.btn_Act5.setText('')
        self.btn_Act5.clicked.connect(self.__btn_XXXX_Pass)

    def __btn_About_Clicked(self):
        self.__btn_XXXX_Disconnect()
        self.wgt_Tools.setVisible(True)
        self.btn_Act1.setText('檢視說明')
        self.btn_Act1.clicked.connect(self.__btn_XXXX_Pass)
        self.btn_Act2.setText('關於本程式(~)')
        self.btn_Act2.clicked.connect(self.__act_About_Triggered)
        self.btn_Act3.setText('')
        self.btn_Act3.clicked.connect(self.__btn_XXXX_Pass)
        self.btn_Act4.setText('')
        self.btn_Act4.clicked.connect(self.__btn_XXXX_Pass)
        self.btn_Act5.setText('')
        self.btn_Act5.clicked.connect(self.__btn_XXXX_Pass)

    def __btn_XXXX_Pass(self):
        pass

    def __btn_XXXX_Disconnect(self):
        self.btn_Act1.disconnect()
        self.btn_Act2.disconnect()
        self.btn_Act3.disconnect()
        self.btn_Act4.disconnect()
        self.btn_Act5.disconnect()

# ========================================================================
    # Func:登入帳號
    def __act_login(self):
        if self.__credential['token']:
            reply = QtWidgets.QMessageBox.warning(self.__thisWindow, '登入帳號',
                    '已登入帳號，是否重新登入?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                state = UserHandle.user(self.__setting, self.__thisWindow)
            else:
                return
        else:
            state = UserHandle.user(self.__setting, self.__thisWindow)
        if not state:
            QtWidgets.QMessageBox.warning(self.__thisWindow,'登入帳號', '登入失敗')
        else:
            QtWidgets.QMessageBox.information(self.__thisWindow,'登入帳號', '登入成功')

    # Func:設定checkBox狀態
    def __checkBoxStateSetup(self):
        if self.__setting['Auto_Select_Video'] == True:
            self.checkBox_AutoSelectVideo.setChecked(True)
        if self.__setting['Random_Add_Video'] == True:
            self.checkBox_RandomAddingVideo.setChecked(True)

    # Func:確認是否有憑證，與憑證是否過期
    def checkCredentials(self):
        if not self.__setting['API_Key'] and not self.__credential['token']:
            QtWidgets.QMessageBox.warning(self.__thisWindow, '查無可用憑證',
                    '請至少選擇登入帳號或者更新API_Key其一')
            return False
        if self.__credential['token']:
            credentials = GO2_credentials.Credentials.from_authorized_user_file("Source_Other/credentialsFile.json")
            if not credentials.valid:   #如果access過期則自動更新
                req = GAT_requests.Request()
                error = credentials.refresh(req)
                if error:
                    QtWidgets.QMessageBox.information(self.__thisWindow,'憑證過期', '更新憑證失敗')
                    return
                else:
                    with open("Source_Other/credentialsFile.json", "w") as credenFile:
                        credenFile.write(credentials.to_json())
                    self.__credential = credentials.to_json()
        return  True

    #Thread:列出預設國家名稱
    def __getCountryCodeThread(self):
        dict = vh_Handle.getCountryCode() #更新Return:Dict['國家']='code'
        if dict is None:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '取得國家代碼失敗')
            return
        self.cbb_HotVideoCategories.clear()
        for tmp in dict.keys():
            self.cbb_HotVideoCategories.addItems([tmp])
        self.__country_code = dict
        self.cbb_HotVideoCategories.setCurrentIndex(0)
        self.cbb_HotVideoCategories.setEnabled(True)
        self.btn_GetHotViedoList.setEnabled(True)

    # Func:啟動執行緒獲得並顯示要搜尋熱門影片的國家
    def __setCountryName(self): #已修復
        if not self.trd_VideoList.is_alive():
            trd_PlayVideo = threading.Thread(target=self.__getCountryCodeThread)
            trd_PlayVideo.setDaemon(True)
            trd_PlayVideo.start()
        else:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '請稍後再試')

    # Func:checkbox狀態改變時更改setting
    def __checkboxsStateChanged(self):
        if self.checkBox_RandomAddingVideo.isChecked():
            self.__setting['Random_Add_Video'] = True
        else:
            self.__setting['Random_Add_Video'] = False
        if self.checkBox_AutoSelectVideo.isChecked():
            self.__setting['Auto_Select_Video'] = True
        else:
            self.__setting['Auto_Select_Video'] = False
        with open("Source_Other/setting.json","w") as settingfile:
                json.dump(self.__setting,settingfile)

    # Event:取得所選國家的熱門影片
    def btn_GetHotViedoList_Click(self):
        if self.checkCredentials() == True:
            country_Code = self.__country_code[self.cbb_HotVideoCategories.currentText()]
            videoData = VideoClass.YoutubeVideo(listID=country_Code)
            if not videoData or not videoData.filtered:
                QtWidgets.QMessageBox.information(self.__thisWindow, '取得影片失敗',
                        '取得影片失敗，請登入帳號或更新 api key 後再試一次。')
                return
            if self.checkBox_AutoSelectVideo.isChecked():
                tmp = {}
                if not videoData.filtered:
                    tmp[videoData.v_title] = videoData.v_id
                else:
                    self.__getVideoAutomatically(videoData.filtered,tmp)
            else:
                DialogWindow = DialogClass.VideoDialog()
                DialogWindow.setupUi()
                ui = form_VideoList.Form_VideoList()
                ui.setupUi(DialogWindow)
                ui.setFormOpacity(self.hs_Opacity.value() / 10)
                self.trd_VideoList = threading.Thread(
                    target=self.__getVideoThread,
                    args=[videoData.filtered,ui])
                self.trd_VideoList.setDaemon(True)
                self.trd_VideoList.start()
                DialogWindow.exec_()
                try:
                    trd_Handle.stop_thread(self.trd_VideoList)
                except Exception as e:
                    print('停止執行緒')
                if not ui.getDialogResault():
                    return
                tmp = ui.getDataList()
            if not tmp:
                QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '獲取熱門影片失敗')
                return
            if self.checkBox_RandomAddingVideo.isChecked():
                for key in tmp:
                    self.__clipboard.append(key)
                random.shuffle(self.__clipboard)
                self.lsw_VideoList.addItems(self.__clipboard)
            else:
                self.lsw_VideoList.addItems(key for key in tmp)
            self.__clipboard = []
            self.i_PlayList = {**self.i_PlayList, **tmp}
        else:
            return

    # Event:加入單影片至清單
    def __btn_AddVideoUrl_Click(self):
        if self.checkCredentials() == True:
            filteredVideoID = vh_Handle.getYoutubeIDFromUrl(self.txt_VideoUrl.toPlainText())
            videoData = VideoClass.YoutubeVideo(videoID=filteredVideoID)
            if not videoData or not videoData.v_title and not videoData.filtered:
                QtWidgets.QMessageBox.information(self.__thisWindow, '取得影片失敗',
                        '輸入網址或ID錯誤，或者目標影片為私人或已刪除影片。\n如果自己是私人影片的擁有者，請登入帳號後再試一次。')
                return
            if self.checkBox_AutoSelectVideo.isChecked():
                tmp = {}
                if not videoData.filtered:
                    tmp[videoData.v_title] = videoData.v_id
                else:
                    self.__getVideoAutomatically(videoData.filtered,tmp)
            else:
                DialogWindow = DialogClass.VideoDialog()
                DialogWindow.setupUi()
                ui = form_VideoList.Form_VideoList()
                ui.setupUi(DialogWindow)
                ui.setFormOpacity(self.hs_Opacity.value() / 10)
                if not videoData.filtered:
                    ui.setListItem(videoData.v_img, videoData.v_title, videoData.v_id, videoData.v_autor)
                else:
                    self.__getVideoThread(videoData.filtered,ui)
                DialogWindow.exec_()
                if not ui.getDialogResault():
                    return
                tmp = ui.getDataList()
            if not tmp:
                QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '獲取影片失敗')
                return
            if self.checkBox_RandomAddingVideo.isChecked():
                for key in tmp:
                    self.__clipboard.append(key)
                random.shuffle(self.__clipboard)
                self.lsw_VideoList.addItems(self.__clipboard)
            else:
                self.lsw_VideoList.addItems(key for key in tmp)
            self.__clipboard = []
            self.i_PlayList = {**self.i_PlayList, **tmp}
        else:
            return

    # Event:加入影片清單至清單
    def __btn_AddVideoListUrl_Click(self):
        check = self.checkCredentials()
        if check == True:
            inputtedListID = vh_Handle.getYoutubeIDFromUrl(self.txt_VideoUrl.toPlainText(),thisIsPlayList=True)
            videoData = VideoClass.YoutubeVideo(listID=inputtedListID)
            if not videoData or not videoData.v_title and not videoData.filtered:
                QtWidgets.QMessageBox.information(self.__thisWindow, '取得影片失敗',
                        '取得清單影片，請登入帳號後再試一次。')
                return
            if self.checkBox_AutoSelectVideo.isChecked():
                tmp = {}
                if not videoData.filtered:
                    tmp[videoData.v_title] = videoData.v_id
                else:
                    self.__getVideoAutomatically(videoData.filtered,tmp)
            else:
                DialogWindow = DialogClass.VideoDialog()
                DialogWindow.setupUi()
                ui = form_VideoList.Form_VideoList()
                ui.setupUi(DialogWindow)
                ui.setFormOpacity(self.hs_Opacity.value() / 10)
                self.trd_VideoList = threading.Thread(
                    target=self.__getVideoThread,
                    args=[videoData.filtered, ui])
                self.trd_VideoList.setDaemon(True)
                self.trd_VideoList.start()
                DialogWindow.exec_()
                try:
                    trd_Handle.stop_thread(self.trd_VideoList)
                except Exception as e:
                    print('停止執行緒')
                if not ui.getDialogResault():
                    return
                tmp = ui.getDataList()
            if not tmp:
                QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '獲取影片清單失敗')
                return
            if self.checkBox_RandomAddingVideo.isChecked():
                for key in tmp:
                    self.__clipboard.append(key)
                random.shuffle(self.__clipboard)
                self.lsw_VideoList.addItems(self.__clipboard)
            else:
                self.lsw_VideoList.addItems(key for key in tmp)
            self.__clipboard = []
            self.i_PlayList = {**self.i_PlayList, **tmp}
        else:
            return    

    #Thread:將播放清單內的影片陳列出來
    def __getVideoThread(self,videoData,form_VideoList):
        if not videoData:
            form_VideoList.showErrorMessage('獲取影片資料失敗')
        else:
            form_VideoList.videoCount = len(videoData)
            for videoInfo in range(len(videoData)):
                v_id = str(videoData[videoInfo].get('vid'))
                v_img = str(videoData[videoInfo].get('vimg'))
                v_title = str(videoData[videoInfo].get('vtitle'))
                v_uploader = str(videoData[videoInfo].get('vuploader'))
                form_VideoList.setListItem(v_img, v_title, v_id, v_uploader)
                form_VideoList.setListModel()
    
    #Fun: 自動選擇所有影片
    def __getVideoAutomatically(self,videoData,tmp):
        for index in range(len(videoData)):
            tmp[videoData[index].get('vtitle')] = videoData[index].get('vid')
        return tmp

    # Event:影片清單雙擊事件
    def __lsw_VideoList_DoubleClick(self, evt):
        if self.lsw_VideoList.currentRow() >= 0:
            DialogWindow = DialogClass.VideoDialog()
            DialogWindow.setupUi()
            ui = form_VideoInfo.Form_VideoInfo()
            ui.setupUi(DialogWindow)
            ui.setFormOpacity(self.hs_Opacity.value() / 10)
            ui.displayVideoInfo(self.i_PlayList[self.lsw_VideoList.item(
                self.lsw_VideoList.currentRow()).text()])
            ui.trd_Title.setDaemon(True)
            ui.trd_Title.start()
            DialogWindow.exec_()
            if ui.trd_Title.is_alive():
                trd_Handle.stop_thread(ui.trd_Title)

    def __btn_close_Clicked(self):
        self.__thisWindow.close()

    def __btn_WgtClose_Clicked(self):
        if self.wgt_Tools.isVisible():
            self.wgt_Tools.setVisible(False)

    def __btn_min_Clicked(self):
        self.__thisWindow.showMinimized()

    # Event:循序播放按鈕事件 #未修-關聯項目SQLClass.Form_Web.azure floder
    def __btn_SequentialPlayVideo_Click(self):
        data = self.lsw_VideoList.selectedIndexes()
        if not data:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '尚未選擇影片')
            return
        data.sort()
        resault = SQLClass.SQLHandle.createLocalVideoTable('list', 'VideoList')
        if not resault:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '建立資料表失敗')
            return
        for tmp in data:
            resault = SQLClass.SQLHandle.insertLocalSQLTable(
                'list', 'VideoList',
                self.lsw_VideoList.item(int(tmp.row())).text(),
                self.i_PlayList[self.lsw_VideoList.item(int(
                    tmp.row())).text()])
            if not resault:
                QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '寫入資料表失敗')
                return
        self.__thisWindow.hide()
        #        resault = subprocess.call(['YoutubePlayer.exe'],
        #                                  cwd=os.getcwd(),
        #                                  shell=True)
        #        if resault:
        #            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息',
        #                                           '找不到播放器(YoutubePlayer.exe)')
        app = QtWidgets.QApplication.instance()
        WebWindow = DialogClass.VideoDialog()
        ui = form_Web.Form_Web()
        ui.setupUi(WebWindow)
        ui.setFormOpacity(self.hs_Opacity.value() / 10)
        WebWindow.exec_()
        self.__thisWindow.show()

    def mouseMoveEvent(self,event):
        print('100')

    # Event:選單->新建清單事件
    def __act_NewFile_Triggered(self):
        self.i_PlayList.clear()
        self.lsw_VideoList.setCurrentItem(None)
        self.lsw_VideoList.clear()
        self.i_ListName = None
        self.lbl_FileName.setText(self.__str_WindowsTitle + '［］')

    # Event:選單->開啟清單事件
    def __act_ReadFile_Triggered(self):
        ui = FileClass.FileHandle()
        str_FileName = ui.readFileByDialog('./save/', 'Video List', '.vls')
        if str_FileName:
            self.i_ListName = str_FileName
            self.lbl_FileName.setText(self.__str_WindowsTitle + '［' + self.i_ListName + '］')
            data = ui.getData()
            self.i_PlayList = data[1]
            self.lsw_VideoList.setCurrentItem(None)
            self.lsw_VideoList.clear()
            self.lsw_VideoList.addItems(tmp for tmp in data[0])
        elif str_FileName is None:
            self.i_ListName = None
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '檔案讀取失敗')
        else:
            return

    # Event:選單->儲存清單事件
    def __act_SaveFile_Triggered(self):
        data, items = [], []
        if self.i_ListName is None:
            self.__act_SaveNewFile_Triggered()
            return
        ui = FileClass.FileHandle()
        for x in range(0, self.lsw_VideoList.count()):
            items.append(self.lsw_VideoList.item(x).text())
        data.append(items)
        data.append(self.i_PlayList)
        ui.setData(data)
        str_FileName = ui.saveFile(self.i_ListName)
        if str_FileName:
            QtWidgets.QMessageBox.information(self.__thisWindow, '消息提示', '儲存成功')
            self.i_ListName = str_FileName
        elif str_FileName is None:
            self.i_ListName = None
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '檔案寫入失敗')
        else:
            return

    # Event:選單->另存清單事件
    def __act_SaveNewFile_Triggered(self):
        data, items = [], []
        ui = FileClass.FileHandle()
        for x in range(0, self.lsw_VideoList.count()):
            items.append(self.lsw_VideoList.item(x).text())
        data.append(items)
        data.append(self.i_PlayList)
        ui.setData(data)
        str_FileName = ui.saveFileByDialog('./save/', 'Video List', '.vls')
        if str_FileName:
            self.i_ListName = str_FileName
            self.lbl_FileName.setText(self.__str_WindowsTitle + '［' +
                                      self.i_ListName + '］')
            QtWidgets.QMessageBox.information(self.__thisWindow, '消息提示', '儲存成功')
        elif str_FileName is None:
            self.i_ListName = None
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '檔案寫入失敗')
        else:
            return

    # Event:選單->關閉事件
    def __act_CloseForm_Triggered(self):
        if self.wgt_Tools.isVisible():
            self.wgt_Tools.setVisible(False)
        else:
            self.__thisWindow.close()

    # Event:選單->剪下事件
    def __act_Cut_Triggered(self):
        self.__act_Copy_Triggered()
        self.__act_Delete_Triggered()

    # Event:選單->複製事件
    def __act_Copy_Triggered(self):
        list, dict = [], {}
        data = self.lsw_VideoList.selectedIndexes()
        data.sort()
        for tmp in data:
            list.append(self.lsw_VideoList.item(int(tmp.row())).text())
            dict[self.lsw_VideoList.item(int(
                tmp.row())).text()] = self.i_PlayList[self.lsw_VideoList.item(
                    int(tmp.row())).text()]
        self.__clipboard, self.__cliptmp = list, dict

    # Event:選單->貼上事件
    def __act_Paste_Triggered(self):
        try:
            if len(self.__clipboard) > 0:
                if self.lsw_VideoList.currentIndex().row() < 0:
                    index = self.lsw_VideoList.count() - 1
                else:
                    index = self.lsw_VideoList.currentIndex().row()
                self.lsw_VideoList.insertItems(index + 1, self.__clipboard)
                self.i_PlayList = {**self.i_PlayList, **self.__cliptmp}
                for i in range(index if index >= 0 else 0,
                               index + len(self.__clipboard) + 1):
                    self.lsw_VideoList.item(i).setSelected(True)
        except Exception as e:
            print('項目貼上失敗:' + str(e))
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '貼上失敗')

    # Event:選單->刪除事件
    def __act_Delete_Triggered(self):
        if self.lsw_VideoList.count() > 0:
            data = self.lsw_VideoList.selectedIndexes()
            data.sort()
            data.reverse()
            for tmp in data:
                self.lsw_VideoList.takeItem(int(tmp.row()))

    # Event:選單->全選事件
    def __act_SelectAll_Triggered(self):
        if self.lsw_VideoList.count() > 0:
            self.lsw_VideoList.setCurrentItem(None)
            for i in range(0, self.lsw_VideoList.count()):
                self.lsw_VideoList.item(i).setSelected(True)

    # Event:選單點擊展開事件
    def __menu_CloudHandle_Triggered(self):
        if not self.__str_UserName is None:
            self.act_Connect.setChecked(True)
            self.act_DeleteSpecificList.setEnabled(True)
            self.act_CreateNewListOnYoutube.setEnabled(True)
        else:
            self.act_Connect.setChecked(False)
            self.act_DeleteSpecificList.setEnabled(False)
            self.act_CreateNewListOnYoutube.setEnabled(False)

    # Event:選單->API_Key設定事件
    def __act_InputAPIkey_Triggered(self):
        DialogWindow = DialogClass.VideoDialog()
        ui = form_Cloud.Form_Cloud()
        ui.setupUi(DialogWindow)
        DialogWindow.exec_()
        if ui.getAcceptResault():
            api_key = ui.txt_API_key.text().strip()
            if api_key != self.__setting['API_Key']:
                self.__setting['API_Key'] = api_key
                with open("Source_Other/setting.json", "w") as settingfile:
                    json.dump(self.__setting,settingfile)

    # Event:選單->建立新YT清單事件
    def __act_CreateNewListOnYoutube_Triggered(self):
        DialogWindow = DialogClass.VideoDialog()
        ui = form_Cloud.Form_Cloud()
        ui.setupUi(DialogWindow)
        DialogWindow.exec_()
        if ui.getAcceptResault():
            #新增清單
            inputtedNewListData = [ui.txt_NewList_Title.text(), ui.txt_NewList_Descript.text(), ui.listPrivacy]
            print('add list start')
            res = VideoClass.YoutubeVideo(newListData=inputtedNewListData)
            print(res.insertListData)
            if res.insertListData:
                print('建立新清單完成，name: '+ res.insertListData['snippet']['title'])
                #插入影片至清單
                    #測試thread功能
                insertRes = VideoClass.YoutubeVideo(insertVideoID=self.i_PlayList,targetListID=res.insertListData['id'])
                if insertRes.errorFlag == True:
                    print('create list and insert video complete but some video insert failed.')
                    QtWidgets.QMessageBox.information(self.__thisWindow, '新增完成', '新清單建立完成')
                else:
                    print('create list and insert video complete')
                    QtWidgets.QMessageBox.information(self.__thisWindow, '新增完成', '新清單建立完成')

            else:
                print('add playlist faild')
                QtWidgets.QMessageBox.information(self.__thisWindow, '新增失敗', '建立新播放清單時失敗')

    # Event:選單->刪除YT清單事件
    def __act_DeleteSpecificList_Triggered(self):
        DialogWindow = DialogClass.VideoDialog()
        ui = form_Cloud.Form_Cloud()
        ui.setupUi(DialogWindow)
        DialogWindow.exec_()
        if ui.getAcceptResault():
            listID = vh_Handle.getYoutubeIDFromUrl(ui.txt_delete_target.text(),thisIsPlayList=True)
            res = VideoClass.YoutubeVideo(targetListID=listID)
            if res.errorFlag == True:
                QtWidgets.QMessageBox.information(self.__thisWindow, '刪除失敗', '發生問題，清單可能刪除失敗')
            else:
                QtWidgets.QMessageBox.information(self.__thisWindow, '刪除完成', '刪除清單完成')

    # Event:選單->導出Txt事件
    def __act_Txt_Triggered(self):
        list = []
        if self.lsw_VideoList.count() <= 0:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '清單為空')
            return
        handle = FileClass.FileHandle()
        for x in range(0, self.lsw_VideoList.count()):
            video_title = '{0:s}:'.format(self.lsw_VideoList.item(x).text())
            list.append(video_title + 'https://youtu.be/' +
                        self.i_PlayList[self.lsw_VideoList.item(x).text()])
        handle.setData(list)
        str_FileName = handle.saveTxtByDialog('./save/output/')
        if str_FileName is None:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '導出記事本失敗')

    # Event:選單->導出Excel事件
    def __act_Excel_Triggered(self):
        tmp = []
        list = []
        if self.lsw_VideoList.count() <= 0:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '清單為空')
            return
        handle = FileClass.FileHandle()
        for x in range(0, self.lsw_VideoList.count()):
            tmp.clear()
            tmp.append(self.lsw_VideoList.item(x).text())
            tmp.append('https://youtu.be/' +
                       self.i_PlayList[self.lsw_VideoList.item(x).text()])
            list.append(tmp.copy())
        handle.setData(list)
        str_FileName = handle.saveExcelByDialog('./save/output/')
        if str_FileName is None:
            QtWidgets.QMessageBox.critical(self.__thisWindow, '錯誤訊息', '導出活頁簿失敗')

    # Event:選單->關於事件
    def __act_About_Triggered(self):
        DialogWindow = QtWidgets.QDialog()
        ui = form_About.Form_About()
        ui.setupUi(DialogWindow)
        DialogWindow.exec_()
