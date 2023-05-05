import json
import google.oauth2.credentials as GO2_credentials
import googleapiclient.discovery as GAC_Dis
import googleapiclient.errors as GAC_Error
# //////////////////////////////////////////////////////////////
import os
# *Disable OAuthlib's HTTPS verification when running locally.
# !DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
# //////////////////////////////////////////////////////////////

#透過傳入需求(影片、清單ID、熱門影片國家碼)呼叫API來取得影片詳細資訊 屬性:(圖片,標題,影片ID,作者,評價,上傳日期,瀏覽次數)
#Argument:Youtube影片ID/無
class YoutubeVideo:
    v_id, v_img, v_title, v_autor, v_like, v_dislike, v_upload_date, v_views = (
        '', '', '', '', '', '', '', '')
    country, playlist_id, filtered, maxResults, insertVideoID, insertListData, targetListID, errorFlag = (
        '', '', '', '', '', '','','')

    def __init__(self, videoID=None,listID=None, newListData=None, insertVideoID=None, targetListID=None):
        self.v_id, self.v_img, self.v_title, self.v_autor, self.v_like, self.v_dislike, self.v_upload_date, self.v_views = (
            '', '', '', '', '', '', '', '')
        self.country, self.playlist_id, self.filtered, self.maxResults, self.insertVideoID, self.insertListData, self.targetListID, self.errorFlag = (
            '', '', '','','','','',False)

        try:
            if videoID:     # *如果不是空值或None
                if type(videoID) == list:
                    self.v_id = ','.join(videoID)
                    self.__getMultiVideo()
                else:
                    self.v_id = videoID
                    self.__getVideoDetails()
            elif listID:
                if type(listID) == list:
                    self.playlist_id = listID
                    self.__getMultiPlayListVideoDeatils()
                elif listID.startswith('PL'):
                    self.playlist_id = listID
                    self.__getPlayListVideoDeatils()
                else:
                    self.country = listID
                    self.__getMostPopularVideoDeatils()
            #----以下為登入才可用的API------------------------------------------------
            elif newListData:
                self.playlist_insert(newListData[0], newListData[1], newListData[2])
            elif insertVideoID and targetListID:
                self.__insertVideoIntoList(insertVideoID, targetListID)
            elif targetListID:
                self.__deleteList(targetListID)
            else:
                print('傳入資料不正確或為None')
                return None
        except Exception as e:
            print('取得影片資料時發生錯誤: '+str(e))
            return None

    #刪除清單
    def __deleteList(self, targetListID):
        if type(targetListID) == str:
            res = self.playlist_delete(targetListID)
            if res:
                self.errorFlag = True
        else:
            for index in targetListID:
                res = self.playlist_delete(index)
                if res:
                    self.errorFlag = True

    #新增影片到清單內
    def __insertVideoIntoList(self,targetVideo, targList):
        for index in targetVideo.values():
            res = self.playlistItems_insert(targList, index)
            if not res or res != '500':
                self.errorFlag = True

    #取得發燒影片資料
    def __getMostPopularVideoDeatils(self):
        try:
            filteredData = []
            res = self.videos_list_mostPopular(self.country)
            expactVideoCount = res.get('pageInfo').get('totalResults')
            nextPageToken = res.get('nextPageToken')
            if nextPageToken == None:
                self.getVidData(filteredData,res,expactVideoCount)
            else:
                self.getVidData(filteredData,res,self.maxResults)
                while nextPageToken != None:
                    nextResponse = self.videos_list_mostPopular(self.country,nextPageToken)
                    nextPageToken = nextResponse.get('nextPageToken')
                    self.getVidData(filteredData,nextResponse,self.maxResults)
            self.filtered = filteredData
        except Exception as e:
            print('發生錯誤: {0}'.format(e))

    #取得複數影片資料
    def __getMultiVideo(self):
        try:
            filteredData = []
            res = self.videos_list(self.v_id)
            expactVideoCount = res.get('pageInfo').get('totalResults')
            self.getVidData(filteredData,res,expactVideoCount)
            self.filtered = filteredData
        except Exception as e:
            print('發生錯誤: {0}'.format(e))

    #取得複數清單影片
    def __getMultiPlayListVideoDeatils(self):
        try:
            filteredData = []
            for playListIndex in range(len(self.playlist_id)):
                res = self.playlistItems_list(self.playlist_id[playListIndex])
                expactVideoCount = res.get('pageInfo').get('totalResults')
                if not 'nextPageToken' in res.keys():
                    self.getVidListData(filteredData,res,expactVideoCount)
                else:
                    nextPageToken = res.get('nextPageToken')
                    self.getVidListData(filteredData,res,self.maxResults)
                    while nextPageToken != None:
                        nextResponse = self.playlistItems_list(self.playlist_id,nextPageToken)
                        nextPageToken = nextResponse.get('nextPageToken')
                        self.getVidListData(filteredData,nextResponse,self.maxResults)
            self.filtered = filteredData
        except Exception as e:
            print('發生錯誤: {0}'.format(e))

    #列出清單內所有影片
    #return data = [{video1 info},{video2 info},...,{video200 info}]
    def __getPlayListVideoDeatils(self):
        try:
            filteredData = []
            res = self.playlistItems_list(self.playlist_id)
            expactVideoCount = res.get('pageInfo').get('totalResults')
            if not 'nextPageToken' in res.keys():
                self.getVidListData(filteredData,res,expactVideoCount)
            else:
                nextPageToken = res.get('nextPageToken')
                self.getVidListData(filteredData,res,self.maxResults)
                while nextPageToken != None:
                    nextResponse = self.playlistItems_list(self.playlist_id,nextPageToken)
                    nextPageToken = nextResponse.get('nextPageToken')
                    self.getVidListData(filteredData,nextResponse,self.maxResults)
            self.filtered = filteredData
        except Exception as e:
            print('發生錯誤: {0}'.format(e))
    
    #過單筆濾影片資料
    def __getVideoDetails(self):
        res = self.videos_list(self.v_id)
        res = res.get('items')[0]
        if not res:     #回傳影片資料為空
            return None
        else:            
            self.v_img = str(res.get('snippet').get('thumbnails').get('default').get('url'))
            self.v_title = str(res.get('snippet').get('title'))
            self.v_autor = str(res.get('snippet').get('channelTitle'))
            self.v_upload_date = str(res.get('snippet').get('publishedAt'))
            self.v_views = str(res.get('statistics').get('viewCount'))
            self.v_like =  str(res.get('statistics').get('likeCount'))
            self.v_dislike =  str(res.get('statistics').get('dislikeCount'))

    #過濾影片資料
    #return dirt[{"id":"","img":"","title":""},...,{"id":"","img":"","title":""}]
    def getVidData(self,filteredData,data,totalVideoCount):
        data = data.get('items')
        try:
            for index in range(totalVideoCount):
                if not data:
                    return filteredData
                else:
                    tmpData = {}
                    tmpData["vid"]= data[index].get('id')
                    tmpData["vimg"] = data[index].get('snippet').get('thumbnails').get('default').get('url')
                    tmpData["vtitle"] = data[index].get('snippet').get('title')
                    tmpData["vuploader"] = data[index].get('snippet').get('channelTitle')
                    filteredData.append(tmpData)
            return filteredData
        except Exception as e:
            if str(e) == 'list index out of range':
                return filteredData
            else:
                print('抓取影片發生預期之外的錯誤'+str(e))
    
    #過濾清單影片的資料
    #return dirt[{"id":"","img":"","title":""},...,{"id":"","img":"","title":""}]
    def getVidListData(self,filteredData,data,totalVideoCount):
        data = data.get('items')
        try:
            for index in range(totalVideoCount):
                if not data:
                    return filteredData
                elif data[index].get('status').get('privacyStatus') == 'private':
                    continue
                else:
                    tmpData = {}
                    tmpData["vid"]= data[index].get('contentDetails').get('videoId')
                    tmpData["vimg"] = data[index].get('snippet').get('thumbnails').get('default').get('url')
                    tmpData["vtitle"] = data[index].get('snippet').get('title')
                    tmpData["vuploader"] = data[index].get('snippet').get('videoOwnerChannelTitle')
                    filteredData.append(tmpData)
        except Exception as e:
            if str(e) == 'list index out of range':
                return filteredData
            else:
                print('抓取清單影片發生預期之外的錯誤'+str(e))

#================================================================
    #API呼叫前置
    def buildApiService(self):
        with open("Source_Other/setting.json", "r") as settingfile:
            build_Params = json.load(settingfile)        
        self.maxResults = build_Params['Vidoe_MaxResults'] #回傳筆數最大值，預設5筆，一次最多50筆。
    
        with open("Source_Other/credentialsFile.json", "r") as settingfile:
            __credential=json.load(settingfile)
        if __credential['token']:
            credentials = GO2_credentials.Credentials.from_authorized_user_file("Source_Other/credentialsFile.json")
            youtube = GAC_Dis.build(build_Params['Api_Service_Name'], build_Params['Api_Version'], credentials=credentials)
        else:
            youtube = GAC_Dis.build(build_Params['Api_Service_Name'], build_Params['Api_Version'], developerKey=build_Params['API_Key'])
        return youtube

    def execute(self, request):
        try:
            return request.execute()
        except GAC_Error.HttpError as e:
                print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))

    #刪除清單
    def playlist_delete(self, playlistID):
        request = self.buildApiService().playlists().delete(
            id = playlistID
            )
        try:
            request.execute()
        except GAC_Error.HttpError as e:
                print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))

    #新增清單
    def playlist_insert(self, title, description, privacy):
        request = self.buildApiService().playlists().insert(
            part = "snippet,status",
            body = {
                "snippet": {
                    "title": title,
                    "description": description,
                    "defaultLanguage": "zh-TW"
                },
                "status": {
                    "privacyStatus": privacy
                }
            }
        )
        try:
            res = request.execute()
            self.insertListData = res if res else None
        except GAC_Error.HttpError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
            self.insertListData = None
    
    # 以清單ID取得清單內所有影片之詳細資料
    def playlistItems_list(self, playlistId, nextPageToken=None):
        request = self.buildApiService().playlistItems().list(
            part = "snippet,contentDetails,status",
            playlistId = playlistId,
            maxResults = self.maxResults,
            pageToken = nextPageToken
        )
        return self.execute(request)    #!

    # 新增影片到清單內
    def playlistItems_insert(self, playlistId, videoId, position=0):
        request = self.buildApiService().playlistItems().insert(
            part = "snippet",
            body = {
                "snippet": {
                    "playlistId": playlistId,
                    "position": position,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": videoId
                    }
                }
            }
        )
        try:
            request.execute()
        except GAC_Error.HttpError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
            return e.status_code
    
    #videos這支api會直接略過私人或已刪除影片
    def videos_list(self, videoId):
        request = self.buildApiService().videos().list(
            part = "snippet,statistics",
            id = videoId
        )
        return self.execute(request)    #!

    # 取得影片資訊或當下發繞影片資料(200部)，可選擇影片類型跟地區，預設台灣跟音樂
    def videos_list_mostPopular(self, countryCode, nextPageToken=None, category=10):
        request = self.buildApiService().videos().list(
            part = "snippet,id,status",
            chart = "mostPopular",
            maxResults = self.maxResults,
            regionCode = countryCode,
            videoCategoryId = category,
            pageToken = nextPageToken
        )
        return self.execute(request)    #!
