import sys
sys.path.append('..')
import os
import time
import requests
import Source_Ui.UI_VideoList as UI_VideoList

from PyQt5 import QtCore, QtGui, QtWidgets

#加入影片對話視窗
class Form_VideoList(UI_VideoList.Ui_ListWindows):
    model = None
    __dialogResault = False
    __selectedItems = {}
    __nameTemp = []
    __itemTemp = {}
    __thisWindow = None
    videoCount=0
    timer=None
    checked_indexs = []

    #Func:設定視窗內元件
    def setupUi(self, form_VideoList):
        super(Form_VideoList, self).setupUi(form_VideoList)

        scriptDir = os.path.abspath(__file__)
        # self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'logo.png'))
        #設定無邊框透明視窗
        form_VideoList.setWindowOpacity(0.9)
        form_VideoList.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        form_VideoList.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        form_VideoList.setFixedSize(form_VideoList.size())
        form_VideoList.setWindowIcon(QtGui.QIcon(scriptDir+'../img/icon/icon_VideoInfo.ico'))

        #設定[全選]按鈕樣式
        self.ckb_Check.setStyleSheet("""
            QCheckBox{font-family: "Microsoft JhengHei";font-size: 14px;color: rgb(255, 255, 255);border-top-left-radius:10px;border-bottom-left-radius:10px;border-top-right-radius:10px;border-bottom-right-radius:10px;}
            QCheckBox::indicator {margin-left:5px;width: 50px;height: 50px;}
            """)
            # QCheckBox::indicator:unchecked {image: url(./img/icon/uncheckedd.png)}
            # QCheckBox::indicator:checked {image: url(./img/icon/checked.png)}
        #設定清單樣式
        self.lsv_VideoList.setStyleSheet("""
            QListView::item {margin-top:10px;}
            QListView::indicator{width: 50px;height: 50px;margin-right:10px;}
            """)
            # QListView::indicator:checked { image: url(./img/icon/checked.png)}
            # QListView::indicator:unchecked { image: url(./img/icon/unchecked.png)}
        #設定清單卷軸樣式
        self.lsv_VideoList.horizontalScrollBar().setStyleSheet("""
            QScrollBar:horizontal {height: 8px;background: #DDD;}
            QScrollBar::handle:horizontal {background: #AAA;}
            QScrollBar::handle:horizontal:hover {background: #888;}
            QScrollBar::sub-line:horizontal, QScrollBar::add-line:horizontal {width: 0;height: 0;}
            """)
        self.lsv_VideoList.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {width: 8px;background: #DDD;padding-bottom: 8px;}
            QScrollBar::handle:vertical {background: #AAA;}
            QScrollBar::handle:vertical:hover {background: #888;}
            QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {width: 0;height: 0;}
            """)

        self.__thisWindow = form_VideoList
        self.model = QtGui.QStandardItemModel() #建立清單模組
        self.checked_indexs.clear()  #清空使用者選擇的項目編號
        self.__selectedItems.clear()  #清空使用者選擇的項目內容
        self.__nameTemp.clear()  #清空所有項目標題
        self.__itemTemp.clear()  #清空所有項目標題與ID
        self.model.clear()  #清空清單模組內項目
        self.timer = QtCore.QTimer()  #建立定時器用於標題跑馬燈
        self.timer.start(1000)  #1秒執行一次
        self.lsv_VideoList.setModel(self.model) #將模組設為清單內容
        self.__setEventHandle(form_VideoList) #綁定元件事件
        self.__dialogResault = False #預設傳達視窗回傳為False,按送出則為True

    # Func:綁定按鈕事件
    def __setEventHandle(self, form_VideoList):
        self.lsv_VideoList.doubleClicked.connect(
            self.__lsv_VideoList_DoubleClicked) #影片清單項目雙擊選取
        self.ckb_Check.clicked.connect(
            self.__ckb_Check_StateChanged)  #勾選後全選項目
        self.btn_Commit.clicked.connect(self.__btn_Commit_Clicked)  #送出選擇的項目
        self.btn_Cancel.clicked.connect(self.__btn_Cancel_Clicked)  #取消
        self.btn_close.clicked.connect(self.__btn_close_Clicked)  #關閉視窗
        self.timer.timeout.connect(self.__tick)  #每秒檢查載入清單進度

    # Func:設定視窗透明度
    def setFormOpacity(self,value):
        self.__thisWindow.setWindowOpacity(value)

    # Func:此為定時器,每秒檢查載入清單進度
    def __tick(self):
        #若項目總數大於0則開始檢查
        if self.videoCount>0:
            #計算單個項目相較於項目數量的百分比
            step = 100.0 / self.videoCount
            #若視窗關閉則停止定時器
            if not self.__thisWindow.isVisible():
                print('載入中斷')
                self.timer.stop()
            else:
                #按照目前清單內項目數量,設定載入百分比
                self.pb_Process.setValue(self.lsv_VideoList.model().rowCount()*step)
        #若是清單內項目數量大於等於項目總數,則設定為100%,代表完成
        if self.lsv_VideoList.model().rowCount()>=self.videoCount:
            self.pb_Process.setValue(100)
            print('清單載入完成')
            self.timer.stop()

    # Event:勾選後全選
    def __ckb_Check_StateChanged(self):
        #若清單內無項目則返回並不執行
        if self.lsv_VideoList.model().rowCount()<=0:
            return
        Checked=False
        if self.ckb_Check.isChecked():
            Checked=True
        #將清單內每個項目,按照[全選]勾選狀態,設定勾選狀態
        for index in range(self.lsv_VideoList.model().rowCount()): #逐一取得每個項目
            m_index = QtCore.QModelIndex()
            m_index.child(index, 0)
            if Checked:
                #如果[全選]勾選則設定勾選
                self.model.item(index).setData(QtCore.QVariant(QtCore.Qt.Checked), QtCore.Qt.CheckStateRole)
            else:
                #如果[全選]未勾選則設定未勾選
                self.model.item(index).setData(
                    QtCore.QVariant(QtCore.Qt.Unchecked),
                    QtCore.Qt.CheckStateRole)

    # Event:雙擊選項自動選取
    def __lsv_VideoList_DoubleClicked(self):
        index = self.lsv_VideoList.currentIndex().row()
        if self.lsv_VideoList.model().item(index).checkState() == QtCore.Qt.Checked: #如果已經勾選則取消勾選
            self.model.item(index).setData(QtCore.QVariant(QtCore.Qt.Unchecked), QtCore.Qt.CheckStateRole)
        else:  #如果未勾選則勾選
            self.model.item(index).setData(
                QtCore.QVariant(QtCore.Qt.Checked), QtCore.Qt.CheckStateRole)


    # Event:點擊確認後將所選項目存入__selectedItems
    def __btn_Commit_Clicked(self):
        for index in range(self.lsv_VideoList.model().rowCount()): #逐一取得所有項目
            m_index = QtCore.QModelIndex()
            m_index.child(index, 0)
            if self.lsv_VideoList.model().item(index).checkState(
            ) == QtCore.Qt.Checked:  #項目勾選則將編號記錄到checked_indexs
                self.checked_indexs.append(index)
        #按照checked_indexs紀錄的編號將項目放到__selectedItems,__nameTemp包含影片名稱,__itemTemp可取得影片ID
        for index in self.checked_indexs:
            self.__selectedItems[self.__nameTemp[index]] = self.__itemTemp[
                self.__nameTemp[index]]
        self.__dialogResault = True #傳達使用者按了送出而不是取消
        self.__thisWindow.close() #關閉視窗

    # Event:取消按鈕
    def __btn_Cancel_Clicked(self):
        self.__thisWindow.close()

    # Event:關閉視窗
    def __btn_close_Clicked(self):
        self.__thisWindow.close()

    # Func:取得所選項目__selectedItems
    def getDataList(self):
        if len(self.__selectedItems) > 0:
            return self.__selectedItems
        else:
            return None

    # Func:回傳使用者確認或者取消
    def getDialogResault(self):
        return self.__dialogResault if len(self.__selectedItems) > 0 else False

    # Func:設定列表後hide()->show()強制刷新列表
    def setListModel(self):
        self.lsv_VideoList.hide()
        self.lsv_VideoList.setModel(self.model)  #將清單模組設定為清單內容
        self.lsv_VideoList.show()

    # Func:設定列表每行項目元件內容
    #Argument:圖片網址,影片標題,影片ID Return:無 (Error: Alert Dialog)
    def setListItem(self, IMG, TITLE, ID, UPLOADER):
        try:
            #讀取縮圖
            requests.urllib3.disable_warnings()
            rs = requests.session()
            ir = rs.get(IMG, verify=False)
            file_adress = "img\\" + ID + '.jpg'
            if ir.status_code == 200:
                open(file_adress, 'wb').write(ir.content)
            image = QtGui.QPixmap()
            image.load(file_adress)
            image = image.scaled(100, 100, QtCore.Qt.KeepAspectRatio)

            #設定每行項目內每個元件的內容
            item = QtGui.QStandardItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable
                          | QtCore.Qt.ItemIsEnabled)
            item.setData(
                QtCore.QVariant(QtCore.Qt.Unchecked), QtCore.Qt.CheckStateRole) #勾選欄
            item.setData(
                QtCore.QVariant(QtGui.QPixmap(image)),
                QtCore.Qt.DecorationRole)  #圖片欄
            count = self.model.rowCount() + 1
            item.setData(
                QtCore.QVariant("第" + str(count) + "筆  影片ID：" + ID + "\n標題：" + TITLE +
                                "\n上傳者：" + UPLOADER),
                QtCore.Qt.DisplayRole)  #內文欄
            self.__nameTemp.append(TITLE)  #儲存每個項目的影片標題  (供最後回傳時查詢用)
            self.__itemTemp[TITLE] = ID  #儲存每個項目的影片標題以及影片ID (供最後回傳時查詢用)
            self.model.appendRow(item)  #將此行加入清單模組
        except Exception as e:
            print('項目設定失敗:' + str(e))
