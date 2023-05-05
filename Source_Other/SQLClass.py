import sqlite3
import pyodbc


class SQLHandle():

    __server = 'school-hw.database.windows.net'
    __database = 'ScriptHW'
    __username = 'test'
    __password = 'Abc123456789'
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                self.__server + ';PORT=1443;DATABASE=' + self.__database +
                ';UID=' + self.__username + ';PWD=' + self.__password +
                ';charset=' + "utf8")
            self.cursor = self.connection.cursor()
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()

    #連線網路資料庫
    #Argument:無 Return:True Or False (Error:False)
    def connectSQL(self):
        try:
            self.connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                self.__server + ';PORT=1443;DATABASE=' + self.__database +
                ';UID=' + self.__username + ';PWD=' + self.__password +
                ';charset=' + "utf8")
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()
            return False

    #建立網路資料表
    #Argument:資料表名稱 Return:True Or False (Error:False)
    def createVideoTable(self, NAME):
        try:
            sql = """DROP TABLE IF EXISTS """ + NAME + """;"""
            self.cursor.execute(sql)
            sql = """CREATE TABLE """ + NAME + """ (
            VIDEO_ID ntext,
            VIDEO_TITLE ntext)"""
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()
            return False

    #插入內容到網路資料表
    #Argument:資料表名稱,影片ID,影片標題 Return:True Or False (Error:False)
    def insertVideoTable(self, TABLE_NAME, VIDEO_ID, VIEDO_TITLE):
        sql = """INSERT INTO """ + TABLE_NAME + """(VIDEO_ID,VIDEO_TITLE)VALUES (N'""" + VIDEO_ID + """', N'""" + VIEDO_TITLE + """')"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()
            return False

    #查詢網路資料表內容
    #Argument:資料表名稱 Return:list=[影片標題,..],dict[標題]=影片ID (Error:None,None)
    def selectVideoTable(self, TABLE_NAME):
        dict = {}
        list = []
        sql = """SELECT * FROM """ + TABLE_NAME
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                list.append(row[1])
                dict[row[1]] = row[0]
            return list, dict
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()
            return None, None

    #關閉網路資料庫連線
    #Argument:無 Return:True Or False (Error:False)
    def close(self):
        try:
            self.connection.close()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            self.connection.rollback()
            return False

    #建立本地資料表
    #Argument:資料庫檔名,資料表名稱 Return:True Or False (Error:False)
    def createLocalVideoTable(DB_NAME, TABLE_NAME):
        try:
            conn = sqlite3.connect(DB_NAME + '.db')
            c = conn.cursor()
            c.execute('''DROP TABLE IF EXISTS ''' + TABLE_NAME + ''';''')
            c.execute('''CREATE TABLE ''' + TABLE_NAME + '''
                      (videoTitle  TEXT,
                       videoID   TEXT);''')
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            return False

    #查詢本地資料表
    #Argument:資料庫檔名,資料表名稱,查詢欄位 Return:list=[][] (Error:None)
    def selectLocalSQLTable(DB_NAME, TABLE_NAME, TEXT):
        return_resault = []
        try:
            conn = sqlite3.connect(DB_NAME + '.db')
            c = conn.cursor()
            sql = "SELECT " + TEXT + " FROM " + TABLE_NAME
            resault = c.execute(sql)
            for row in resault:
                return_resault.append([row[0], row[1]])
            conn.commit()
            conn.close()
            return return_resault
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            return None

    #插入本地資料表
    #Argument:資料庫檔名,資料表名稱,影片標題,影片ID Return:True Or False (Error:False)
    def insertLocalSQLTable(DB_NAME, TABLE_NAME, videoTitle, videoID):
        try:
            conn = sqlite3.connect(DB_NAME + '.db')
            c = conn.cursor()
            sql = """INSERT INTO '""" + TABLE_NAME + """'(videoTitle, videoID) VALUES ('{}','{}');""".format(
                videoTitle.strip(), videoID.strip())
            c.execute(sql)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print('資料庫錯誤:' + str(e))
            return False