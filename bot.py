# 기본 세팅
import discord
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv() # .env로 설정한 환경 변수를 불러온다.
DISCORD_API_KEY = os.getenv("") # 환경 변수로 설정한 Discord API KEY를 가져온다. # 디스코드 봇 토큰 정보는 매우 중요한 정보이다 절때 깃허브에 유출 금지!
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    pprint("Ready to connect to discord ") # 봇을 켤수 있을때 디버깅 메시지

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == "!hello" or message.content == "!hi":
        await message.channel.send("Hello!") #Hello라고 메시지 보내기

@client.event
async def on_connect():
    pprint("connect to discord") # 봇이 디스코드에 접속했을때

@client.event
async def on_disconnect():
    pprint("disconnect to discord") #봇이 디스코드에서 접속이 끊겼을때

if __name__ == "__main__":
	# run() 인자로 Discord API KEY를 넘겨준다.
    client.run(DISCORD_API_KEY)

#~~이제 어떤 기능 추가하지...?~~
