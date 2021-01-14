#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for symptom
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_symptom = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_symptom:
        print("[symptom] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我][一直]拉肚子":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我][一直]跑廁[所]":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我][上][廁所]的[頻率]增加":
        # write your code here
        resultDICT["symptom"] = "泌尿"
        pass

    if utterance == "[我][大]便出血[絲]":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我][晚上]要睡著會忘記呼吸":
        # write your code here
        if "忘記" in inputSTR and "呼吸" in inputSTR:
            resultDICT["symptom"] = "耳鼻喉" 
        pass

    if utterance == "[我][最近][一直]咳嗽":
        # write your code here
        resultDICT["symptom"] = "耳鼻喉" 
        pass

    if utterance == "[我][每日][一][腹瀉]":
        # write your code here
        resultDICT["symptom"] = args[3]
        pass

    if utterance == "[我][賀爾蒙]失調":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]做過[心導管手術]":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]坐著有暈眩的[感覺]":
        # write your code here
        if "暈眩" in inputSTR:
            resultDICT["symptom"] = "耳鼻喉"
        pass

    if utterance == "[我]想吐":
        # write your code here
        if "想吐" in inputSTR:
            resultDICT["symptom"] = "家醫"
        pass

    if utterance == "[我]拉肚子":
        # write your code here
        resultDICT["symptom"]="腸胃"
        pass

    if utterance == "[我]會[忽然]抖一下":
        # write your code here
        if "抖" in inputSTR:
            resultDICT["symptom"]="神經內"
        pass

    if utterance == "[我]會喘":
        # write your code here
        if "喘" in inputSTR:
            resultDICT["symptom"]="耳鼻喉"
        pass

    if utterance == "[我]會放臭[屁]":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我]有[高血壓][心臟病]":
        # write your code here
        resultDICT["symptom"] = args[1:]
        pass

    if utterance == "[我]有心悸":
        # write your code here
        resultDICT["symptom"] = "心臟"
        pass

    if utterance == "[我]無法行走":
        # write your code here
        resultDICT["symptom"] = "家醫"
        pass

    if utterance == "[我]發燒感冒":
        # write your code here
        if "發燒" in inputSTR and "感冒" in inputSTR:
            resultDICT[""] = "家醫" 
        
        pass

    if utterance == "[我]要驗[B][肝]":
        # write your code here
        if args[2] in inputSTR and args[3] in inputSTR:
            resultDICT[""] ="一般內" 
        pass

    if utterance == "[我]要驗孕":
        # write your code here
        resultDICT["symptom"] = "婦產"
        pass

    if utterance == "[我]覺得缺氧":
        # write your code here
        resultDICT["symptom"] = "胸腔內"
        pass

    if utterance == "[我]食慾不振會[噁心]":
        # write your code here
        resultDICT["symptom"] = "家醫"
        pass

    if utterance == "[我人]會暈":
        # write your code here
        resultDICT["symptom"] = "家醫"
        pass

    return resultDICT