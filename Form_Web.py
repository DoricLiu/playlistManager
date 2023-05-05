import sys
sys.path.append('..')
import cgitb
cgitb.enable(format='text')
import os
import time
import threading
import Source_Other.ThreadHandle as trd_handle
import Source_Other.DialogClass as DialogClass
import Source_Other.SQLClass as SQLClass
import Source_Video.VideoHandle as vh_Handle
import Source_Ui.UI_Web as UI_Web
from PyQt5 import QtGui, QtCore, QtWidgets, QtWebEngineWidgets


class Form_Web(UI_Web.Ui_WebWindow):
    web_Url = ''
    web_Resault = False
    lswStatus = False
    __form_Web = None
    __playlist = {}
    trd_autoPlay = None
    flag_autoPlay = True
    timer = None

    #Func:設定視窗內元件
    def setupUi(self, form_Web):
        super(Form_Web, self).setupUi(form_Web)
        self.__form_Web = form_Web

        #設定無邊框透明視窗
        self.__form_Web.setWindowIcon(QtGui.QIcon('img/icon/icon_Web.ico'))
        self.__form_Web.setWindowOpacity(0.9)
        self.__form_Web.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.__form_Web.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.__playlist.clear()  #清空播放清單
        self.btn_max.setEnabled(False)  #關閉放大按鈕
        self.wgt_right.setVisible(True)  #隱藏右側清單
        self.lswStatus = True  #右側清單狀態為隱藏
        self.__setEventHandle(form_Web)  #綁定元件事件
        self.__setVideoList()  #讀取list.db資料庫
        self.btn_ShowList.setText('▸')  #設定右側清單顯示按鈕圖案
        self.trd_autoPlay = threading.Thread(
            target=self.__listenThread)  #設定自動播放執行緒

    # Func:綁定視窗內元件事件
    def __setEventHandle(self, form_Web):
        #顯示右側清單
        self.btn_ShowList.clicked.connect(self.__btn_ShowList_Clicked)
        #雙擊項目播放
        self.lsw_VideoList.doubleClicked.connect(
            self.__lsw_VideoList_DoubleClicked)
        #播放下一部
        self.btn_Next.clicked.connect(self.__btn_Next_Clicked)
        #播放上一部
        self.btn_Pre.clicked.connect(self.__btn_Pre_Clicked)
        #自動播放
        self.btn_Sequential.clicked.connect(self.__btn_Sequential_Clicked)
        #關閉
        self.btn_close.clicked.connect(self.__btn_close_Clicked)
        #縮小
        self.btn_min.clicked.connect(self.__btn_min_Clicked)

    # Event:關閉
    def __btn_close_Clicked(self):
        self.__form_Web.close()

    # Event:縮小
    def __btn_min_Clicked(self):
        self.__form_Web.showMinimized()

    # Func:設定視窗透明度
    def setFormOpacity(self, value):
        self.__form_Web.setWindowOpacity(value)

    # Func:取得資料庫內所有影片
    def __setVideoList(self):
        data = SQLClass.SQLHandle.selectLocalSQLTable('list', 'VideoList',
                                                      'videoTitle,videoID') #讀取list.db內容
        if data is None:
            QtWidgets.QMessageBox.critical(self.__form_Web, '錯誤訊息', '找不到影片資訊')
        else:
            for tmp in data:
                self.lsw_VideoList.addItem(tmp[0])  #將讀取到的影片標題[0]放入顯示清單
                self.__playlist[tmp[0]] = tmp[1]  #將讀取到的影片標題[0]與影片ID[1]放入清單字典

    # Event:播放下一部影片
    def __btn_Next_Clicked(self):
        #如果清單內沒有項目,標題設定為無
        if self.lsw_VideoList.count() <= 0:
            self.lbl_Title.setText('無')
            return
        #取得目前選取的項目編號,如果編號小於清單內項目總數,則+1到下一項目,並觸發雙擊播放
        index = self.lsw_VideoList.currentIndex()
        index = index.row()
        if index < self.lsw_VideoList.count():
            self.lsw_VideoList.setCurrentRow(index + 1)
        self.__lsw_VideoList_DoubleClicked()

    # Event:播放上一部影片
    def __btn_Pre_Clicked(self):
        #如果清單內沒有項目,標題設定為無
        if self.lsw_VideoList.count() <= 0:
            self.lbl_Title.setText('無')
            return
        #取得目前選取的項目編號,如果編號小於清單內項目總數,則-1到上一項目,並觸發雙擊播放
        index = self.lsw_VideoList.currentIndex()
        index = index.row()
        if self.lsw_VideoList.count() > self.lsw_VideoList.currentRow():
            self.lsw_VideoList.setCurrentRow(index - 1)
        self.__lsw_VideoList_DoubleClicked()

    # Event:雙擊項目建立網頁文檔並播放影片
    def __lsw_VideoList_DoubleClicked(self):
        #如果清單內沒有項目,返回而不執行
        if self.lsw_VideoList.count() <= 0:
            return
        #如果使用者沒選擇項目而雙擊,將選擇項目設為第一項,標題設為標題與(換行)網址
        if self.lsw_VideoList.currentIndex().row() < 0:
            self.lsw_VideoList.setCurrentRow(0)
        self.lbl_Title.setText(
            self.lsw_VideoList.currentItem().text() +
            '\nhttps://youtu.be/' +
            self.__playlist[self.lsw_VideoList.currentItem().text()])
        #利用影片ID產生本地播放網頁index.html
        vh_Handle.runYoutubePlayer(
            self.__playlist[self.lsw_VideoList.currentItem().text()])
        #設定瀏覽器元件網址
        self.setUrl('file:///' + os.getcwd().replace('\\', '/') +
                    '/index.html')
        #刷新瀏覽器
        self.refreshPage()

    # Event:右側影片列表清單(顯示/隱藏)
    def __btn_ShowList_Clicked(self):
        #若清單顯示,則隱藏清單,並且將圖案設成▸
        if self.lswStatus:
            self.wgt_right.setVisible(False)
            self.lswStatus = False
            self.btn_ShowList.setText('▸')
        #若清單未顯示,則顯示清單,並且將圖案設成◂
        else:
            self.wgt_right.setVisible(True)
            self.lswStatus = True
            self.btn_ShowList.setText('◂')

    # Event:自動播放下一部影片
    def __btn_Sequential_Clicked(self):
        #若是目前沒選擇項目,則設為選擇第一項,並雙擊播放
        if self.lsw_VideoList.currentRow() <= 0:
            self.lsw_VideoList.setCurrentRow(0)
            self.__lsw_VideoList_DoubleClicked()
        #若是目前執行緒尚未執行,則開啟執行緒,開啟定時器,成功開啟執行緒則設定按鈕為 ■
        if not self.trd_autoPlay.is_alive():
            self.trd_autoPlay = threading.Thread(target=self.__listenThread)
            self.trd_autoPlay.setDaemon(True)
            self.trd_autoPlay.start()
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.__tick)
            self.timer.start(1000)
            if self.trd_autoPlay.is_alive():
                self.btn_Sequential.setText('■')
        #若是目前執行緒已經執行,則停止執行緒,關閉定時器,設定按鈕為 ↻
        else:
            try:
                trd_handle.stop_thread(self.trd_autoPlay)
            except Exception as ex:
                print('停止執行緒')
            self.timer.stop()
            self.btn_Sequential.setText('↻')

    # Func: Timer每秒檢查是否有完畢訊號,若有則播放下一部
    def __tick(self):
        #若是web_Resault為True,代表影片已播放完畢,則播放下一部
        if self.web_Resault:
            self.__NextVideo()
            self.web_Resault = False
        #如果播放器關閉則把此定時器關閉
        if not self.__form_Web.isVisible():
            self.timer.stop()
        #若執行緒沒運行則定時器關閉
        if not self.trd_autoPlay.is_alive():
            self.timer.stop()

    # Thread: 每秒檢查是否播放完畢,若是則發出完畢訊號
    def __listenThread(self):
        while True:
            #播放器關閉則停止執行緒
            if not self.__form_Web.isVisible():
                break
            #若是web_Resault為True,代表影片已播放完畢,則暫停偵測3秒
            if self.web_Resault:
                time.sleep(3)
            #檢測瀏覽器內是否出現Loading...文字,若有則web_Resault為True,代表影片已播放完畢
            self.listenWeb()
            time.sleep(1)

    # Func: 播放下一部影片
    def __NextVideo(self):
        #如果清單內沒有項目,標題設定為無
        if self.lsw_VideoList.count() <= 0:
            self.lbl_Title.setText('無')
        #取得目前選取的項目編號,如果編號小於清單內項目總數,則+1到下一項目,並觸發雙擊播放
        index = self.lsw_VideoList.currentIndex()
        index = index.row()
        if index < self.lsw_VideoList.count():
            self.lsw_VideoList.setCurrentRow(index + 1)
            self.__lsw_VideoList_DoubleClicked()

    # Func: 設定目前網頁
    def setUrl(self, url):
        self.web_Url = url

    # Func: 刷新網頁頁面
    def refreshPage(self):
        self.wev_WebView.load(QtCore.QUrl(''))
        self.wev_WebView.load(QtCore.QUrl(self.web_Url))

    # Func: 查看是否播放完畢
    def listenWeb(self):
        #檢測瀏覽器內是否出現Loading...文字,若有則web_Resault為True,代表影片已播放完畢
        self.wev_WebView.findText(
            'Loading...', QtWebEngineWidgets.QWebEnginePage.FindFlags(0),
            self.__web_Resault)

    # Func: 查看的結果
    def __web_Resault(self, found):
        self.web_Resault = found


if __name__ == '__main__':
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication([])
        app.aboutToQuit.connect(app.deleteLater)
    else:
        app = QtWidgets.QApplication.instance()
    WebWindow = DialogClass.VideoDialog()
    ui = Form_Web()
    ui.setupUi(WebWindow)
    WebWindow.exec_()
