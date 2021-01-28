#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from med_bot import Result as medBot

DISCORD_TOKEN=""
DISCORD_GUILD="Droidtown Linguistics Tech."
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

@client.event
async def on_message(message):
    if "<@!{}>".format(client.user.id) in message.content:
        
        if "hi!" in message.content:
            response = "我知道這很辛苦但你要加油"
            await message.channel.send(response)
    
        elif 'test' in message.content:
            response = "Send message."
            await message.channel.send(response)
        # here the bot gives answer depended on user's answer to the question ("below 12?")
        elif "y" in message.content:
            userID = str(message.author.id)
            print(userID)
            if userID in responseDICT:
                #the bot has to memorize the user ID in order to know which user it is repsponding to 
                msg = responseDICT[userID]["y"]
                #delete user ID once it get the response from the user
                del responseDICT[userID]
                await message.channel.send(msg)
        elif "n" in message.content:
            userID = str(message.author.id)
            if userID in responseDICT:
                msg = responseDICT[userID]["n"]
                del responseDICT[userID]
                await message.channel.send(msg)        
        
        else:
            msgSTR = message.content.replace("<@!{}> ".format(client.user.id), "")
            response = medBot(msgSTR)
            # since we have set two types of responses here (i.e. ask and msg), we have to separate these two types
            if response["type"] == "ask":
                #set a result element in the dictionary returning from loki first, so we can retrieve it here
                responseDICT[str(message.author.id)] = response["result"]
                await message.channel.send(response["msg"])

            if response["type"] == "msg":
                await message.channel.send(response["msg"])
                
            
        
    elif "bot 點名" in message.content:
        response = "有!"
        await message.channel.send(response)
    


client.run(DISCORD_TOKEN)
