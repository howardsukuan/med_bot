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

LINE_ACCESS_TOKEN   = "aAomwvgmYBfnyZKx3u4+6kQEuCY3aA//QVYg1M6kVBLG3N5KnyaHoj4uHa6LdTKSxfFkw0S+eWqntRJ0ao0DgVPIlVBVcuqUkspr/Vb9Mq2JCuhdjMc4voR/l6J/zZeE6Rzw8AhhB1hmjzhPSS+mMgdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "71b18cd040f6602a0e4e96b35c1a9a52"

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