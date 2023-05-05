
import os
# *Disable OAuthlib's HTTPS verification when running locally.
# !DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
#--------------------------------------------------------------------------------------------
import google_auth_oauthlib.flow as accessFlow
import time
import threading
import Source_Other.ThreadHandle as trd_Handle
import sys
from PyQt5 import QtWidgets, QtCore
sys.path.append('..')

class user():
    res_credentials = None

    def __init__(self, current_setting, ui):
        self.ui = ui
        self.signIn_timeout = current_setting['SignIn_Timeout']     # 等待timeout秒數
        self.one_step_login()

    '''
    如果登入過程中斷，程式會卡在等待監聽狀態中導致無回應，因此改用執行緒執行登入，
    等待預設的秒數(timeout)之後再詢問使用者是否已登入過程，若結束則停止執行緒，反之則繼續等待。
    若結束執行緒時未取得任何憑證(使用者自行中斷)則回傳空值

    '''
    def one_step_login(self):
        QtCore.pyqtRemoveInputHook()                            # 用來消除警告訊息
        credentials = threading.Thread(target = self.tokenflow)
        credentials.setDaemon(True)
        credentials.start()
        time.sleep(self.signIn_timeout)
        if not self.res_credentials and credentials.is_alive():
            reply = None
            while reply != 'Yes':
                reply = QtWidgets.QMessageBox.warning(self.ui, '登入帳號',
                        '登入時間過長，是否中斷?\n如果已完成登入請選擇"是"',
                        QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.No:
                    reply = 'No'
                    time.sleep(self.signIn_timeout)
                else:
                    reply = 'Yes'
            if not self.res_credentials and credentials.is_alive():
                trd_Handle.stop_thread(credentials)
                print('停止登入')
                return False
            else:
                return True

    #儲存現在時間並進行帳號登入以及授權，帳號授權後將自動回傳code完成後續步驟並回傳憑證
    #將完成後獲得的憑證內使用者資訊轉成 json 並寫入檔案保存，以利之後重新建立完整憑證去呼叫API。
    def tokenflow(self):
        client_secrets_file = "Source_Other/client_secret.json"
        scopes = ["https://www.googleapis.com/auth/youtube.readonly",   #token可訪問的範圍
                    "https://www.googleapis.com/auth/youtubepartner",
                    "https://www.googleapis.com/auth/youtube",
                    "https://www.googleapis.com/auth/youtube.force-ssl"]
        flow = accessFlow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        flow.run_local_server(
                host='localhost',port=8080,
                authorization_prompt_message='Please visit this URL: {url}', 
                success_message='The auth flow is complete; you may close this window.',
                open_browser=True)
        res_credentials = flow.credentials.to_json()
        self.res_credentials = res_credentials
        with open("Source_Other/credentialsFile.json", "w") as credenFile:
            credenFile.write(res_credentials)
