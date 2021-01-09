#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
$ pip3 install flask
"""

from flask import Flask
from flask import request
from flask import jsonify
from line_sdk import Linebot
from med_bot import Result as medBot

LINE_ACCESS_TOKEN   = ""
LINE_CHANNEL_SECRET = ""

app = Flask(__name__)

@app.route("/Robin/", methods=["GET", "POST"])
def webhook():
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
                    reply = medBot(dataDICT["message"])#"可以去腸胃科看診"
                    print("debug.msg:{}".format(reply))
                    linebot.respText(dataDICT["replyToken"], reply) #回應的內容 放在裡面dataDICT
                    #從這裡接Loki

        return jsonify({"status": True, "msg": "Line Webhook Success."})

    # OTHER
    else:
        return jsonify({"status": False, "msg": "HTTP_405_METHOD_NOT_ALLOWED"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)