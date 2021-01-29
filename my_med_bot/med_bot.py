#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

import requests
try:
    from intent import Loki_Emergency
    from intent import Loki_Gender
    from intent import Loki_body_part
    from intent import Loki_symptom
except:
    from .intent import Loki_Emergency
    from .intent import Loki_Gender
    from .intent import Loki_body_part
    from .intent import Loki_symptom


LOKI_URL = ""
USERNAME = ""
LOKI_KEY = ""

# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []

        try:
            result = requests.post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": INTENT_FILTER
            })

            if result.status_code == requests.codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Emergency
                if lokiRst.getIntent(index, resultIndex) == "Emergency":
                    resultDICT = Loki_Emergency.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Gender
                if lokiRst.getIntent(index, resultIndex) == "Gender":
                    resultDICT = Loki_Gender.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # body_part
                if lokiRst.getIntent(index, resultIndex) == "body_part":
                    resultDICT = Loki_body_part.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # symptom
                if lokiRst.getIntent(index, resultIndex) == "symptom":
                    resultDICT = Loki_symptom.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

#This is a dictionary for the possible symptoms and bodyparts that could be uncomfortable for the patients 
DepartmentDICT = {
  **dict.fromkeys(["顎","耳朵","鼻子","鼻","咽喉","顎","鼻涕", "喉嚨", "喉部", "脖子", "耳", "鼻樑", "鼻腔內", "耳鼻喉", "鼻炎", "打呼", "打鼾", "扁桃腺", "流鼻血", "過敏性鼻炎"], "耳鼻喉科"), 
  **dict.fromkeys(["肚子","腸胃", "胃"], "腸胃科"),
  **dict.fromkeys(["頸椎","喉部","嘴", "風池穴", "小腿", "臉頰", "屁股", "眉間", "頭", "頸部", "頸部", "腹瀉", "家醫", "頭痛", "頭暈", "咳嗽", "噁心","小拇指", "下背", "發燒", "疲勞", "疲倦", "暈眩","背","累"], "家醫科"),
  **dict.fromkeys(["陰部", "婦產", "乳房", "乳腺", "陰道"], "婦產科"),
  **dict.fromkeys(["腹", "高血壓", "黃疸","一般內科"], "一般內科"),
  **dict.fromkeys(["心臟", "瓣膜", "心", "心導管手術","心跳"], "心臟內科"),
  **dict.fromkeys(["胸口", "胸"], "胸腔外科"),
  **dict.fromkeys(["眼睛", "飛蚊症", "眼"], "眼科"), 
  **dict.fromkeys(["泌尿"], "泌尿科"), 
  **dict.fromkeys(["賀爾蒙"], "內分泌科"),
  **dict.fromkeys(["泌尿", "小便", "尿"], "泌尿科"),
  **dict.fromkeys(["神經內","麻痺"], "神經內科"),
  **dict.fromkeys(["胸腔內"], "胸腔內科"),
  **dict.fromkeys(["牙齒"], "牙科"),
  **dict.fromkeys(["掉頭髮"], "皮膚科")
}

#this is a function for matching the department with the bodypart or symptom
def FindDepartment(inputSTR):
    inputLIST = [inputSTR]
    try:
        resultDICT = runLoki(inputLIST)
        symptom = resultDICT["symptom"]
        return DepartmentDICT[symptom]   
    except:
        pass
    try:
        resultDICT = runLoki(inputLIST)
        bodypart = resultDICT["bodypart"]
        return DepartmentDICT[bodypart] 
    except:       
        return "尚未解決QQ 這部分會盡速處理！"


# in this function, we set a dictionary for each response
# a special key 'result' is set to the dictionary which appears when the user mentions about their children
def Result(inputSTR):
    Emergency = ["大量出血","昏迷","失去意識","沒有心跳","血流不止","停止呼吸"]
    ChildLIST = ["小孩","孩子","女兒","兒子"]
    department= FindDepartment(inputSTR)
    if any (eme in inputSTR for eme in Emergency):
        response = {"type":"msg","msg": "請立即打119"}
        return response
    
    elif any (chi in inputSTR for chi in ChildLIST):
        response = {"type":"ask", "msg": "請問是否為12歲(包含12)以下的小孩?填入y/n",
                    "result":{"y":"可以去小兒科看診", "n":"{dep} 謝謝!".format(dep=department)}}
        return response
        
    else:
        response = {"type":"msg","msg": "{dep} 謝謝!".format(dep=department)}
        return response    
        
        
    
if __name__ == "__main__":
    inputSTR = "我過敏"
    print(Result(inputSTR))