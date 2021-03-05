## 看病小幫手 My MedBot
「肚子有點痛」

「怎麼辦，心臟有點痛」

不知道你會不會有時候覺得這裡痛、那裡痛，但是不確定要看哪科？

上網查覺得有點懶，然後問櫃台的人員覺得有點害羞

那看病小幫手就是你最好的夥伴，是一個醫療分科機器人，只要詢問他就可以得到看哪科的建議喔~ 

你是怎麼問醫院服務台的人，就怎麼問看病小幫手!!!

## 使用步驟
1. 加入 my_med_bot 到discord 
   邀請Link: https://discord.gg/yRCp2PjF
   
   
2.Tag my_med_bot, 例如 @my_med_bot 

4. 接著和 my_med_bot 說你哪裡不舒服，可以多說說你是什麼病症，或是哪邊不舒服
   
   @my_med_bot 我喉嚨痛
   
  
  ![喉嚨痛](https://upload.cc/i1/2021/01/29/W4ChRr.png)
   
   
3. 接下來就med bot 就會和你說你可以去哪一科看診喔~ 

## 訓練文本
1. 我們是參考以下網站
    1) 衛生福利部台北醫院就醫指南 https://www.tph.mohw.gov.tw/?aid=12
    2) 臺大醫院 該看哪一科 https://www.ntuh.gov.tw/ntuh/Fpage.action?muid=70&fid=2972
    3) 醫聯網- 醫師獻聲諮詢平台 https://expert.med-net.com/index?gclid=CjwKCAiAp4KCBhB6EiwAxRxbpGjtZfNqJif2RC_sm9_400q7kUImkAYOfqOHxo1n95UHMntRtts1oBoCWUYQAvD_BwE

## 訓練方式 
1. 我們從諮詢論壇、自身經驗和實係測試收集問診的句子。
2. 我們把句子分為兩類：
   1) 身體部位：只要句子中出現身體部位，我們就會分在這個類別
   2) 病症: 只要是
3. 把這兩類句子放入卓騰科技的Loki。接著Loki 就可以把那些句子斷詞，然後整理成不同的句型。依句型分類。
4. 接著把這些問診句子和我們查的資料用python 串接起來，然後回復使用者可以看哪一科
