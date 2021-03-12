#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""

from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot
from med_bot_for_Loki import Result as medBot
#from account_info import accountInfoDICT
LINE_ACCESS_TOKEN   = "5JhPIGnH6FD9znGXM6PG8jgRVWO44ikYUi8r3Y16u5OKfBD1ELFMYo6VdIjKObff9Uxz4WQwimfi7JwrK2/8phv6lxp+X3rx2qvbI8N3JpVvyW0Lj5i6w+Q8E56N51mx6iQDH5Nna1GnhPDy0REWgwdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "7b18d5df4526a0fcc768a171c4c1cc5d"

app = Flask(__name__)
print(app)

@app.route("/callback", methods=["GET", "POST"])

def callback():
    # GET #知道網頁
    if request.method == "GET":
        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # POST
    elif request.method == "POST":
        body = request.get_data(as_text=True)
        signature = request.headers["X-Line-Signature"]

        # Line
        linebot = Linebot(LINE_ACCESS_TOKEN, LINE_CHANNEL_SECRET)

        # dataLIST = [{status, type, message, userID, replyToken, timestamp}] ＃message 比較重要 是送上去的內容 ＃改message 知道要改成蛇內容
        dataLIST = linebot.parse(body, signature)
        for dataDICT in dataLIST:
            print(dataDICT)
            if dataDICT["status"]:
                if dataDICT["type"] == "message":
                    # Send Message
                    #linebot.respText(medBot(dataDICT["message"]), dataDICT["message"])
                    linebot.respText(dataDICT["replyToken"],medBot(dataDICT["message"])["msg"])#回應的內容 放在裡面dataDICT
                    #從這裡接Loki

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})



if __name__ == "__main__":
    app.run()