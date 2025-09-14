# 기본 세팅
import discord
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv() # .env로 설정한 환경 변수를 불러온다.
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY") # 환경 변수로 설정한 Discord API KEY를 가져온다.
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    pprint("Ready to connect to discord ")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == "!hello" or message.content == "!hi":
        await message.channel.send("Hello!")

@client.event
async def on_connect():
    pprint("connect to discord")

@client.event
async def on_disconnect():
    pprint("disconnect to discord")

if __name__ == "__main__":
	# run() 인자로 Discord API KEY를 넘겨준다.
    client.run(DISCORD_API_KEY)

#~~이제 어떤 기능 추가하지...?~~
