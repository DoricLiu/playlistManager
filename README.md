# PlaylistManager
【簡介】
- 製作目的：
  希望至少能達到減少原本合併兩個清單需要點選滑鼠的次數，理想目標則是製作一個清單管理的應用。

- 製作方法：
  使用 Google API Python Client 套件來呼叫YouTube Data V3 API，取得影片或清單資料後進行應用。

- 製作結果：
  使用者輸入影片或清單的網址、ID，並選擇要自動或手動、順序或隨機的方式將影片加入清單，也提供搜尋當下的熱門音樂影片的功能。
  使用模式分成本地或登入帳號兩種：
    1. 本地：透過申請來的 API Key 來呼叫API，但因授權範圍有限，僅能將獲得的影片資訊儲存成本地清單，使用程式內的內嵌網頁來達到播放的目的。
    2. 登入帳號：在登入 YouTube 帳號並授權之後，就能讓使用者將程式內的清單建立到 YouTube 帳號內，同時也能刪除登入帳號所擁有的清單。

----------------------------------------------------------------
【使用方法 & 注意事項】
本程式使用python3.8.5版，確認過符合requirements.txt內的套件版本需求後，執行main.py即可使用。