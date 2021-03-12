# Line_bot 使用說明

## 使用Line: 步驟解說
1. 安裝Line
   請到以下連結下載Line: https://line.me/zh-hant/
   
2. 下載完成後請申請帳號
   
4. 請掃描以下QRcode
   ![](https://upload.cc/i1/2021/03/05/n9Ekzv.png)

5. 接著和 my_med_bot 說你哪裡不舒服，可以多說說你是什麼病症，或是哪邊不舒服，接下來就med bot 就會和你說你可以去哪一科看診喔~

# 3. 開發者說明
## 環境設定
1. 註冊LOKI
2. 註冊 LINE Developer 
3. 註冊 Discord Portal 

## LOKI 使用說明
1. 請到卓騰科技網站 (https://api.droidtown.co/)
2. 連結應用服務，然後選擇LOKI

<img src="https://upload.cc/i1/2021/03/12/CO61Ua.png" width="50%" height="50%" />

3. 進入LOKI後，創一個新的專案，取名為 med_bot
<img src="https://upload.cc/i1/2021/03/12/cvlfjG.png" width="50%" height="50%" />

4. 請到 Ref 文件夾中，到如下圖的地方，上傳這些ref 檔案
<img src="https://upload.cc/i1/2021/03/12/3KDYbW.png" width="50%" height="50%" />

## LINE DEVELOPER 使用說明
1. 請至 LINE DEVELOPER (https://developers.line.biz/zh-hant/) ，以您的Line帳號登入
2. 登入之後，按product，選擇 Message Api 
3. create api 這個畫面中，填入必要內容
4. 在Basic setting 中可以找到您的 LINE secret，請貼到 Line_BOT > line_app 中 LINE secret 地方
5. 在Messaging API 中可以到到您的 LINE token，請貼到 Line_BOT > line_app 中 LINE token 地方

## Discord Portal 使用說明
1. 請至 Discord Portal (https://discord.com/login?redirect_to=%2Fdevelopers) ，使用您的Discord 中帳號登入
2. 看到右上角，按下 new application 
3. 填入您的Discord Bot 名字 
4. 看到左邊的 OAuth2，點下去可以看到 SCOPE 中選 BOT

5. 在OAuth2中的 BOT PERMISSION 點全部
6. 複製 bot 的內容  
----
# 4. 文本訓練方式

## 訓練文本
1. 我們是參考以下網站
    1) 衛生福利部台北醫院就醫指南 https://www.tph.mohw.gov.tw/?aid=12
    2) 臺大醫院 該看哪一科 https://www.ntuh.gov.tw/ntuh/Fpage.action?muid=70&fid=2972
    3) 醫聯網- 醫師獻聲諮詢平台 https://expert.med-net.com/index?gclid=CjwKCAiAp4KCBhB6EiwAxRxbpGjtZfNqJif2RC_sm9_400q7kUImkAYOfqOHxo1n95UHMntRtts1oBoCWUYQAvD_BwE

## 訓練方式 
1. 我們從諮詢論壇、自身經驗和實係測試收集問診的句子。
2. 我們把句子分為兩類：
   1) 身體部位：只要句子中出現身體部位，我們就會分在這個類別，例如手臂斷掉了。
   2) 病症: 只要是和病症相關，或是斷詞後和身體部位斷在一起，例如頭痛，我們就會歸類在此類。
3. 把這兩類句子放入卓騰科技的Loki。接著Loki 就可以把那些句子斷詞，然後整理成不同的句型。依句型分類。
4. 接著把這些問診句子和我們查的資料用python 串接起來，然後回復使用者可以看哪一科。

