import xlwt
import pickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog


class FileHandle(QtWidgets.QWidget):

    data = None

    def __init__(self):
        super(FileHandle, self).__init__()

    #設定要寫入或讀取的Data
    #Argument:要寫入的物件 Return:無
    def setData(self, tmp):
        self.data = tmp

    #取得要寫入或讀取的Data
    #Argument:無 Return:要寫入或讀取的Data
    def getData(self):
        return self.data

    #清除要寫入或讀取的Data
    #Argument:無 Return:無
    def clearData(self):
        self.data = None

    #寫入Data到地址
    #Argument:要寫入的地址 Return:True Or False (Error:False)
    def saveFile(self, str_Path):
        if str_Path is None:
            return False
        else:
            try:
                file = open(str_Path, 'wb')
                pickle.dump(self.data, file)
                file.close()
                return True
            except Exception as e:
                print('檔案儲存失敗:' + str(e))
                return False

    #讀取使用者指定的檔案到Data
    #Argument:窗口預設的讀取地址,讀取檔案的附檔名描述,讀取檔案的附檔名 Return:檔案地址(包含檔名) (Error:None)
    def readFileByDialog(self, str_Path, str_TypeName, str_Type='.txt'):
        file_FileAdress,file_TypeName  = QFileDialog.getOpenFileName(
            self, "選取檔案", str_Path,
            str_TypeName + ' Files (*' + str_Type + ');;All Files (*);')
        if file_FileAdress == '':
            return file_FileAdress
        else:
            try:
                file = open(file_FileAdress, 'rb')
                self.data = pickle.load(file)
                file.close()
                return file_FileAdress
            except Exception as e:
                print('檔案開啟失敗:' + str(e))
                return None

    #寫入Data到使用者指定的檔名與檔案位址
    #Argument:窗口預設的寫入地址,寫入檔案檔名附描述,讀取檔案的附檔名 Return:檔案地址(包含檔名) (Error:None)
    def saveFileByDialog(self, str_Path, str_TypeName, str_Type='.txt'):
        file_FileAdress, file_FileType = QFileDialog.getSaveFileName(
            self, "檔案儲存", str_Path,
            str_TypeName + ' Files (*' + str_Type + ');;All Files (*);')
        if file_FileAdress == '':
            return file_FileAdress
        else:
            try:
                file = open(file_FileAdress, 'wb')
                pickle.dump(self.data, file)
                file.close()
                return file_FileAdress
            except Exception as e:
                print('檔案儲存失敗:' + str(e))
                return None

    #寫入Data到使用者指定的檔名與檔案位址 (Data需為List型式[])
    #Argument:窗口預設的寫入地址,寫入檔案檔名附描述,讀取檔案的附檔名 Return:檔案地址(包含檔名) (Error:None)
    def saveTxtByDialog(self, str_Path, str_TypeName='文字文件', str_Type='.txt'):
        file_FileAdress, file_FileType = QFileDialog.getSaveFileName(
            self, "檔案儲存", str_Path,
            str_TypeName + ' Files (*' + str_Type + ');;All Files (*);')
        if file_FileAdress == '':
            return file_FileAdress
        else:
            try:
                file = open(file_FileAdress, 'w',encoding="utf-8")
                for tmp in self.data:
                    file.write(tmp + '\n')
                file.close()
                return file_FileAdress
            except Exception as e:
                print('檔案儲存失敗:' + str(e))
                return None

    #寫入Data到使用者指定的檔名與檔案位址 (Data需為List型式[][])
    #Argument:窗口預設的寫入地址,寫入檔案檔名附描述,讀取檔案的附檔名 Return:檔案地址(包含檔名) (Error:None)
    def saveExcelByDialog(self,
                          str_Path,
                          str_TypeName='Excel 活頁簿',
                          str_Type='.xls'):
        file_FileAdress, file_FileType = QFileDialog.getSaveFileName(
            self, "檔案儲存", str_Path,
            str_TypeName + ' Files (*' + str_Type + ');;All Files (*);')
        if file_FileAdress == '':
            return file_FileAdress
        else:
            try:
                book = xlwt.Workbook(encoding="utf-8")
                sheet1 = book.add_sheet("影片清單")
                for i in range(0, len(self.data)):
                    sheet1.write(i, 0, self.data[i][0])
                    sheet1.write(i, 1, self.data[i][1])
                book.save(file_FileAdress)
                return file_FileAdress
            except Exception as e:
                print('檔案儲存失敗:' + str(e))
                return None
