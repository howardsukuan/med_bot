#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Gender
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_Gender = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Gender:
        print("[Gender] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]是[一名][女性]":
        # write your code here
        resultDICT["gender"]=args[2] 
        pass

    if utterance == "[我]是[女]的":
        # write your code here
        resultDICT["gender"]=args[1] 
        pass

    if utterance == "我[媽媽]":
        # write your code here
        resultDICT["gender"]=args[0] 
        pass

    return resultDICT