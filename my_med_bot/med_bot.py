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


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
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
    "耳鼻喉科": ["顎", "耳朵", "鼻子", "鼻", "咽喉", "鼻涕", "喉嚨", "脖子", "耳", "鼻樑", "鼻腔內", "耳鼻喉", "鼻炎", "打呼", "打鼾", "扁桃腺", "流鼻血", "過敏性鼻炎"],
    "家醫科": ["喉部", "頸椎", "嘴", "風池穴", "小腿", "臉頰", "屁股", "眉間", "頭", "頸部", "腹瀉", "家醫", "頭痛", "頭暈", "咳嗽", "噁心", "小拇指", "下背", "發燒", "疲勞", "疲倦", "暈眩", "背", "累","臂"],
    "腸胃科": ["肚子", "腸胃", "胃"],
    "婦產科": ["陰部", "婦產", "乳房", "乳腺", "陰道"],
    "一般內科": ["腹", "高血壓", "黃疸", "一般內科"],
    "心臟內科": ["心臟", "瓣膜", "心", "心導管手術", "心跳"],
    "胸腔外科": ["胸口", "胸"],
    "眼科": ["眼睛", "飛蚊症", "眼"],
    "泌尿科": ["泌尿", "小便", "尿"],
    "內分泌科": ["賀爾蒙"],
    "神經內科": ["神經內", "麻痺"],
    "胸腔內科": ["胸腔內"],
    "牙科": ["牙齒"],
    "皮膚科": ["掉頭髮","皮膚","脂肪瘤","痘痘"],
    "身心科":["心情","睡眠"],
    }


#this is a function for matching the department with the bodypart or symptom
def FindDepartment(inputSTR): 
    Emergency = ["大量出血","昏迷","失去意識","沒有心跳","血流不止","停止呼吸"]
    inputLIST = [inputSTR]
    medDICT = {"dep":""}
    resultDICT = runLoki(inputLIST)
    try:
        bodypart = resultDICT["bodypart"]        
        for e in DepartmentDICT.keys():
            if bodypart in DepartmentDICT[e]:
                medDICT["dep"]=e
    except:
        pass
    
    try:
        symptom = resultDICT["symptom"]
        for e in DepartmentDICT.keys():
            if symptom in DepartmentDICT[e]:
                medDICT["dep"]=e  
    except:       
        pass
    
    if medDICT["dep"] == "":
        medDICT["dep"] = "家醫科"
        
    if any (eme in inputSTR for eme in Emergency):
        medDICT["dep"] = "請立即打119"
    
    return medDICT["dep"]
    


# in this function, we set a dictionary for each response
# a special key 'result' is set to the dictionary which appears when the user mentions about their children
def Result(inputSTR):
    department= FindDepartment(inputSTR)
    response = { "msg": "請問是否為12歲(包含12)以下的小孩?填入y/n",
                "result":{"y":"可以去小兒科看診", "n":"請去{dep}".format(dep=department)}}
    return response    
        
        
    
if __name__ == "__main__":
    inputSTR = "我頭暈"
    print(Result(inputSTR))