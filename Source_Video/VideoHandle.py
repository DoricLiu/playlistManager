import sys
sys.path.append('..')

#透過網址取得影片ID
#Argument:Youtube影片網址 Return:影片ID (Error:None)
def __filteID(target,thisIsPlayList):
    try:
        if thisIsPlayList == True:
            if target.find('playlist?list=') > 0:
                    tmp_Id = target.split('playlist?list=')[1]
            else:
                tmp_Id = target.split('&')[1]
                tmp_Id = tmp_Id.split('list=')[1]
        else:
            if target.find('youtu.be') > 0:
                tmp_Id = target.split('youtu.be/')[1]
            else:
                tmp_Id = target.split('v=')[1]
                if tmp_Id.find('&') > 0:
                    tmp_Id = tmp_Id.split('&')[0]
        return tmp_Id
    except:
        print("輸入網址為非預期格式: " + target)
        return None

#確認傳入資料是否為複數，再透過網址取得影片ID
#Argument:Youtube影片網址 Return:影片ID or 'id1,id2...' (Error:None)
def getYoutubeIDFromUrl(target,thisIsPlayList=False):
    try:
        if target.find('://') > 0:      #代表是url
            if target.find(',') > 0:    #若輸入資料內涵','則資料數量為複數
                target = target.split(',')
                tmp_Id = []
                for index in range(len(target)):
                    tmp_Id.append(__filteID(target[index],thisIsPlayList))
                return tmp_Id
            else:
                tmp_Id = __filteID(target,thisIsPlayList)
                return tmp_Id
        else:                           #代表是ID
            if target.find(',') > 0:
                tmp_Id = target.split(',')
            else:
                tmp_Id = target
            return tmp_Id
    except:
        print("輸入網址或ID錯誤: " + target)
        return None

#取得國家名稱及代碼(Dict型式)
#- country code rf: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
#Argument:無 Return:Dict['Country Name']='Country Code' (Error:None) #dict = {'台灣':'TW','美國':'US'}
def getCountryCode():
    try:
        dict = {}
        dict['台灣'] = 'TW'
        dict['美國'] = 'US'
        dict['日本'] = 'JP'
        dict['韓國'] = 'KR'
        return dict                 
    except Exception as e:
        print("發生錯誤:" + str(e))
        return None

#透過影片ID執行Web播放器
#Argument:Youtube影片ID  Return:(Success:True/Error:False)
def runYoutubePlayer(VIDEO_ID):
    file = open("demo.html", "rb")
    content = file.read().decode(errors='ignore')
    content = content.replace('@', '')
    pos = content.find('INSERT_POS')
    if pos != -1:
        content = content[:pos] + VIDEO_ID + content[pos:]
        content = content.replace("INSERT_POS", "")
        file = open("index.html", "w")
        file.write(content)
        file.close()
        url = 'index.html'
        return url
    print('影片執行失敗')
    return None
