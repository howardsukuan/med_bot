#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
from med_bot import Result as medBot

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

@client.event
async def on_message(message):
    msgSTR  = message.content.replace("<@!{}> ".format(client.user.id), "")
    if "<@!{}>".format(client.user.id) in message.content:
        EndConversation = ["謝謝","謝啦","thx","ok","掰","bye"]
        if any (e in msgSTR  for e in EndConversation):
            response = "好的:)"
            await message.channel.send(response)
        else:                
            if msgSTR == "y":
                userID = str(message.author.id)
                print(userID)
                if userID in responseDICT:
                    #the bot has to memorize the user ID in order to know which user it is repsponding to 
                    msg = responseDICT[userID]["y"]
                    #delete user ID once it get the response from the user
                    del responseDICT[userID]
                    await message.channel.send(msg)
            elif msgSTR == "n":
                userID = str(message.author.id)
                if userID in responseDICT:
                    msg = responseDICT[userID]["n"]
                    del responseDICT[userID]
                    await message.channel.send(msg)
                    
            else:
                response = medBot(msgSTR)
                responseDICT[str(message.author.id)] = response["result"]
                await message.channel.send(response["msg"])
                



client.run(DISCORD_TOKEN)
