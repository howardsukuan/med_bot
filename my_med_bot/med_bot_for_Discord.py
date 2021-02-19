#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from med_bot_for_Loki import Result as medBot

DISCORD_TOKEN=""
DISCORD_GUILD="討論小圈圈"
BOT_NAME = "my_med_bot"
#DISCORD_TOKEN=""
#DISCORD_GUILD=""
#BOT_NAME = "my_med_bot"

# Documention
# https://discordpy.readthedocs.io/en/latest/api.html#client

client = discord.Client()
responseDICT = {}

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == DISCORD_GUILD:
            break
    print(f'{BOT_NAME}bot has connected to Discord!')
    print(f'{guild.name}(id:{guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

#訊息正規化: 去除標點，英文大小寫轉換
punctuationSTR = "!@#$%^&*()_+<>?:.,;。，！～~"  # add whatever you want
def str_normalization(inputSTR):
    for w in inputSTR:
        if w in punctuationSTR:
            outputSTR = inputSTR.replace(w, "").lower().strip()
    return outputSTR
    
    
    
    
@client.event
endconversationLIST = ["謝謝","謝啦","thx","ok","掰","bye","掰掰","好喔","你可以退下了"]
yesLIST = ["y","yes","yup","yeah","是","對"]
noLIST = ["n","no","nope","nah","不是","不"]
dontknowLIST = ["idontknow","我不知道","不知道"]
async def on_message(message):
    msgSTR = str_normalization(message.content.replace("<@!{}> ".format(client.user.id), ""))
    if "<@!{}>".format(client.user.id) in message.content:
        if any (e == msgSTR  for e in endconversationLIST ):
            response = "<@!{}>好的:)".format(message.author.id)
            await message.channel.send(response)
        #以下else之後程式碼連續前一輪對話 回傳資訊啟動新的一輪新對話
        else:                
            if any (e == msgSTR  for e in yesLIST):
                userIDSTR = str(message.author.id)
                if userIDSTR in responseDICT:
                    responsemsgSTR = "<@!{}>".format(message.author.id)+responseDICT[userIDSTR]["y"]
                    del responseDICT[userIDSTR]
                    await message.channel.send(responsemsgSTR)
            elif any (e == msgSTR  for e in noLIST):
                if userIDSTR in responseDICT:
                    responsemsgSTR = "<@!{}>".format(message.author.id)+responseDICT[userIDSTR]["n"]
                    del responseDICT[userIDSTR]
                    await message.channel.send(responsemsgSTR)
            elif any (e == msgSTR  for e in dontknowLIST):
                if userIDSTR in responseDICT:
                    responsemsgSTR= "<@!{}>".format(message.author.id)+responseDICT[userIDSTR]["n"]
                    del responseDICT[userIDSTR]
                    await message.channel.send(responsemsgSTR)                
                    
            else: 
                responseDICT[str(message.author.id)] = medBot(msgSTR)["result"]
                await message.channel.send(medBot(msgSTR)["msg"])
                



client.run(DISCORD_TOKEN)
