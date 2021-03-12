#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Emergency
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_Emergency = True
userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Emergency:
        print("[Emergency] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[他]失去意識":
        # write your code here
        pass

    if utterance == "[他]暈倒在[地][上]":
        # write your code here
        pass

    if utterance == "[傷口][大量]出血":
        # write your code here
        pass

    if utterance == "[孩子頭]破了[一個][大洞]":
        # write your code here
        pass

    if utterance == "[我][血流]不止":
        # write your code here
        pass

    if utterance == "[腹部][一直]流血":
        # write your code here
        pass

    return resultDICT