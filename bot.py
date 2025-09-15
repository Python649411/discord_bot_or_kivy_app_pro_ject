# -*- coding: utf-8 -*-
import discord
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv() # .env로 설정한 환경 변수를 불러온다.
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY") # 환경 변수로 설정한 Discord API KEY를 가져온다. # 디스코드 봇 토큰 정보는 매우 중요한 정보이다 절때 깃허브에 유출 금지!
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    pprint("Ready to connect to discord ") # 봇을 켤수 있을때 디버깅 메시지

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == "!안녕" or message.content == "!안녕하세요":
        await message.channel.send("안녕하세요! **깃코프 서버**에 오신걸 환영합니다😁\nHello! Welcome to **Gitcop discord server**😁\nこんにちは！Gitcop discordサーバーへようこそ😁")

    if message.content == "파이썬" or message.content == "!파이썬":
        await message.channel.send("1.print()`print()`는 콘솔에 글자를 남기는 코드입니다 `print()`에 글자를 남길때 **문자열**,**변수**로 글자를 남길수 있습니다 하지만,정수나 다른 값은 넣을수 없습니다\n2.변수 변수는 박스에 값을 넣는겁니다 예: `a = 123`입니다 이 밖에도 다른 코드들을 변수에 저장할수 있습니다\n 3.함수 함수는 def 함수명():(다음줄로 줄바꿈)(들여쓰기 스페이스 4번)실행할코드로 함수를 만들수 있습니다 함수는 특정 코드를 실행하고 결과를 뱉어줍니다 하지만 이렇게 하면 결과를 뱉어만 주지 다른 작업은 안합니다\n그래서 실행할 코드를 a = 실행할 코드로 변수를 만들고 a 변수를 쓸 곳에 씁니다\n그리고 return a로도 할수 있습니다 그리고 ()안에 self같은 매개변수를 넣을수 있습니다\n4.불리언은 true(참),false(거짓),not(반대로),and입니다\n예:print(1 > 3)의 값은 false입니다\nprint(1 < 3)은 true입니다\nnot은 true,false값은 반대로 바꾸는겁니다\n예:not true => false\nnot false => true 입니다\n.and은 true and true에서 true밖에 없습니다 그럼 출력이 true입니다\nfalse and false는 false밖에 없으니 출력이 false입니다\n하지만 true and false의 출력은 false입니다\nfalse and true의 출력은 true입니다\n비교 연산자는 ==(같음)\n!=(같지 않음)\n<(작음)\n>(큼)\n<=(작거나 같음)\n>=(크거나 같음)입니다 정수,소수점에서 사용할수 있고 변수에 정수 또는 소수점이 들어가 있으면 변수에다 사용할수 있습니다\n5.import import은 라이브러리를 불러오는 코드입니다 예:import 라이브러리 이름 또한 라이브러리는 `pip install 라이브러리 이름`으로 설치할수 있습니다 또한 수많은 라이브러리가 있습니다") #사용자가 !hello 또는 !hi라고 입력했을때 봇이 Hello!라고 말하기

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
