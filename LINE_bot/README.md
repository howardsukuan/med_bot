# Line_bot 使用說明

# 使用者說明
## 使用Line: 步驟解說
1. 安裝Line
   請到以下連結下載Line: https://line.me/zh-hant/
   
2. 下載完成後請申請帳號
   
4. 請掃描以下QRcode
   ![](https://upload.cc/i1/2021/03/05/n9Ekzv.png)

5. 接著和 my_med_bot 說你哪裡不舒服，可以多說說你是什麼病症，或是哪邊不舒服，接下來就med bot 就會和你說你可以去哪一科看診喔~

# 開發者說明

## LINE DEVELOPER 使用說明
1. 請至 LINE DEVELOPER (https://developers.line.biz/zh-hant/) ，以您的Line帳號登入
2. 登入之後，按product，選擇 Message Api 

<img src="https://upload.cc/i1/2021/03/12/31OUhy.png" width="50%" height="50%" />

3. create api 中設定以下5項必要資訊，了解LINE Official Account Terms of Use 和 LINE official Account API Terms of Use 之後，點下Create 
   a. Provider: 請選擇 create a new provider，然後下面的名字可以自己取名 (以本圖為例，取作 MED_BOT) 

 <img src="https://upload.cc/i1/2021/03/12/i9gxDm.png" width="50%" height="50%" />

   b. Channel name: 請自行取名 channel name 這裡是您LINE 的名字 
   c. Channel description: 請描述此聊天機器人用途
   d. Category: 請選擇您的聊天機器人的服務內容範圍 (e.g. 醫療相關) 
   e. Subcategory: 選擇細項的內容服務
   

6. 在Basic setting 中可以找到您的 LINE secret，請貼到 line_app 檔案取代原本 accountInfoDICT["LINE_CHANNEL_SECRET"] (line 15)

例如 : LINE_CHANNEL_SECRET = "your secret"

8. 在Messaging API 中可以到到您的 LINE token，請貼到 line_app 檔案取代原本 accountInfoDICT["LINE_ACCESS_TOKEN"] (line 14)

例如 : LINE_ACCESS_TOKEN   = ""
