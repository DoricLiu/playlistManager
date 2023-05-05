import sys
sys.path.append('..')

import time
import threading
import requests
import os
import Source_Video.VideoClass as VideoClass
import Source_Ui.UI_VideoInfo as UI_VideoInfo

from PyQt5 import QtCore, QtGui, QtWidgets


class Form_VideoInfo(UI_VideoInfo.Ui_InfoWindows):
    video = None
    image = None
    __thisWindow=None
    trd_Title=None

    #Func:設定視窗內元件
    def setupUi(self, form_VideoInfo):
        super(Form_VideoInfo, self).setupUi(form_VideoInfo)

        #設定無邊框透明視窗
        form_VideoInfo.setWindowOpacity(0.9)
        form_VideoInfo.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        form_VideoInfo.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        form_VideoInfo.setFixedSize(form_VideoInfo.size())
        form_VideoInfo.setWindowIcon(
            QtGui.QIcon('img/icon/icon_VideoInfo.ico'))

        self.__thisWindow = form_VideoInfo
        self.__setEventHandle(form_VideoInfo)  #綁定元件事件
        self.trd_Title = threading.Thread(
            target=self.__titleThread)  #設定自動播放執行緒

    # Func:設定視窗透明度
    def setFormOpacity(self, value):
        self.__thisWindow.setWindowOpacity(value)

    # Func:綁定按鈕事件
    def __setEventHandle(self, form_VideoInfo):
        self.btn_close.clicked.connect(self.__btn_close_Clicked) #關閉視窗

    # Event:關閉視窗
    def __btn_close_Clicked(self):
        self.__thisWindow.close()

    # Thread:影片標題跑馬燈
    def __titleThread(self):
        loop = 60 #影片標題欄填滿空格為60格
        videoTitle = str(self.lbl_Title.text())  #影片標題
        if len(videoTitle) > 20:  #影片標題大於20字則開啟跑馬燈
            while True:
                #每0.05秒將標題前的60個空格逐一消除
                for i in range(loop):
                    time.sleep(0.05)
                    self.lbl_Title.setText(' '*(loop-i) + videoTitle[0:i])
                #每0.05秒在標題後逐一增加空格,數量為60+標題字數三倍
                for i in range(loop+(len(videoTitle)*3)):
                    time.sleep(0.05)
                    self.lbl_Title.setText(videoTitle + ' ' * (i))

    # Func:顯示影片資訊
    #Argument:影片ID Return:無
    def displayVideoInfo(self, VIDEO_ID):
        #透過影片ID取得影片資訊
        self.video = VideoClass.YoutubeVideo(videoID=VIDEO_ID)
        #檢查縮圖是否存在
        saved_Img = os.listdir('img')
        if VIDEO_ID+'.jpg' not in saved_Img:
            #透過影片縮圖網址抓圖並存檔
            url = self.video.v_img
            requests.urllib3.disable_warnings()
            rs = requests.session()
            ir = rs.get(url, verify=False)
            file_adress = "img\\" + str(self.video.v_id) + '.jpg'
            if ir.status_code == 200:
                open(file_adress, 'wb').write(ir.content)
        else:
            file_adress = "img\\" + VIDEO_ID + '.jpg'
            pass

        #將視窗內的標籤設定為影片資訊
        self.lbl_Title.setText(self.video.v_title) #標題
        self.lbl_Autor.setText(self.video.v_autor) #作者
        self.lbl_UploadDate.setText(self.video.v_upload_date.split('T')[0])  #上傳日期
        self.lbl_Views.setText(self.video.v_views)  #瀏覽次數
        self.lbl_Rate.setText('Like(' + self.video.v_like + ')　' + 'Dislike(' +
                              self.video.v_dislike + ')')  #喜歡以及不喜歡人數

        #讀取圖片到graphicsView視窗
        try:
            self.image = QtGui.QPixmap()
            path = file_adress
            self.image.load(path)  #從Path讀取縮圖
            self.image = self.image.scaledToWidth(248, QtCore.Qt.SmoothTransformation) #強制影片寬度
            self.__loadImage()
        except Exception as e:
            print('載入圖片錯誤:' + str(e))

    # Func:載入影片縮圖
    def __loadImage(self):
        self.graphicsView.scene = QtWidgets.QGraphicsScene()
        item = QtWidgets.QGraphicsPixmapItem(self.image)
        self.graphicsView.scene.addItem(item)
        self.graphicsView.setScene(self.graphicsView.scene)
