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
    if utterance == "[我]一直拉肚子":
        # write your code here
        if "拉肚子" in inputSTR:
            resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我]一直跑廁所":
        # write your code here
        if "跑廁所" in inputSTR:
            resultDICT["symptom"] = "腸胃"         
        pass

    if utterance == "[我]上[廁所]的[頻率]增加":
        # write your code here
        resultDICT["symptom"] = "泌尿"
        pass

    if utterance == "[我][大]便出血[絲]":
        # write your code here
        resultDICT["symptom"] = "腸胃"
        pass

    if utterance == "[我]晚上要睡著會忘記呼吸":
        # write your code here
        if "忘記" in inputSTR and "呼吸" in inputSTR:
            resultDICT["symptom"] = "耳鼻喉" 
        pass

    if utterance == "[我][最近][一直]咳嗽":
        # write your code here
        if "咳嗽" in inputSTR :
            resultDICT["symptom"] = "家醫"        
        pass

    if utterance == "[我]每日[一][腹瀉]":
        # write your code here
        resultDICT["symptom"] = args[2]
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
        if "吐" in inputSTR:
            resultDICT["symptom"] = "家醫"
        if "痣" in inputSTR:
            resultDICT["symptom"] = "皮膚"
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

    if utterance == "[我]會放[臭屁]":
        # write your code here
        if "屁" in inputSTR:
            resultDICT["symptom"] = "腸胃"    
        pass

    if utterance == "[我]有[高血壓][心臟病]":
        # write your code here
        resultDICT["symptom"] = args[1]
        pass

    if utterance == "[我]有心悸":
        # write your code here
        if "心悸" in inputSTR:
            resultDICT["symptom"] = "心臟"         
        pass

    if utterance == "[我]無法行走":
        # write your code here
        resultDICT["symptom"] = "家醫"
        pass

    if utterance == "[我]發燒感冒":
        # write your code here
        if "發燒" in inputSTR or "感冒" in inputSTR:
            resultDICT["symptom"] = "家醫"        
        pass

    if utterance == "[我]要驗[B][肝]":
        # write your code here
        if args[2] in inputSTR and args[3] in inputSTR:
            resultDICT["symptom"] ="一般內" 
        pass

    if utterance == "[我]要驗孕":
        # write your code here
        if "驗孕" in inputSTR:
            resultDICT["symptom"] = "婦產" 
        pass

    if utterance == "[我]覺得缺氧":
        # write your code here
        if "缺氧" in inputSTR:
            resultDICT["symptom"] = "胸腔內" 
        pass

    if utterance == "[我]食慾不振會[噁心]":
        # write your code here
        if "食慾不振" in inputSTR:
            resultDICT["symptom"] = "家醫"
        if "瘋" in inputSTR:
            resultDICT["symptom"] = "身心"
        pass
    
    if utterance == "[我人]會暈":
        # write your code here
        if "暈" in inputSTR:
            resultDICT["symptom"] = "頭暈"        
        pass
    if utterance == "我持續頭暈快[兩個月]":
        # args [兩個月] 
        if "暈" in inputSTR:
            resultDICT["symptom"] = "頭暈"  
    if utterance == "我暈眩":
        # args []
        if "暈眩" in inputSTR:
            resultDICT["symptom"] = "頭暈"  
    if utterance == "發燒了":
        if "發燒" in inputSTR:
            resultDICT["symptom"] = "家醫" 
    if utterance == "感冒了":
        if "感冒" in inputSTR:
            resultDICT["symptom"] = "家醫" 
    if utterance == "我有點[疲勞]":
        resultDICT["symptom"] = args[0]
    if utterance == "頭痛":
        # args []
        if "乳房" in inputSTR:
            resultDICT["symptom"] = "婦產"
        else:
            resultDICT["symptom"] = "頭痛"
    if utterance == "黃疸":
        # args []
        resultDICT["symptom"] = "腸胃"
    if utterance == "流鼻血":
        # args []
        resultDICT["symptom"] = "家醫"
    if utterance == "高血壓":
        # args []
        resultDICT["symptom"] = "一般內科"
    if utterance == "過敏":
        # args []   
        resultDICT["symptom"] = "家醫"
    if utterance == "我有[脂肪瘤]":
        # args [脂肪瘤]
        resultDICT["symptom"] = args[0]
    if utterance == "我[一直]長[痘痘]":
        # args [一直, 痘痘]
        resultDICT["symptom"] = args[1]
    
    if utterance == "瘋了":
        # args []
        if "瘋" in inputSTR:
            resultDICT["symptom"] = "身心"
            
    if utterance == "[我]禿了":
        # args [朋友]
        if "禿" in inputSTR:
            resultDICT["symptom"] = "皮膚" 
    
    if utterance == "[我]骨折了":
        # args [我]
        if "骨折" in inputSTR:
            resultDICT["symptom"] = "骨科"       

    return resultDICT