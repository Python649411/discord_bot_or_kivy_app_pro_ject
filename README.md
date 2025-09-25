# discord_bot_pro_ject
디스코드 봇 만들기
`**지우 참여!**` `**진민형 참여!**`
# 봇 만들기 직전에 !!!!필독!!!!
# 메시지 기능 사용법
bot.py에`20번`줄과`21번`줄에 이런 코드가 있다
```
if message.content == "" or message.content == "":
    await message.channel.send()
```
### 이 코드는 사용자가 뭐라 또는 뭐라 메시지를 입력 했을때 봇이 메시지를 보내는 코드다
`if message.content == ""` 이 코드에서 `""`문자열에 뭘 쓰냐면 사용자가 **뭐라** 보냈을때의 if문이다

그리고
```
or message.content == ""
```
이게 있는데 이건 **뭐라 또는 뭐라**다
이렇게 활용이 가능하다
```
if message.content == "!안녕" or message.content == "!안녕하세요":
    await message.channel.send()
```
#다음단계
```
await message.channel.send()
```
이 코드는 뭐라 또는 뭐라 => `if message.content == "" or message.content == "":`
이걸 세팅 했을때 쓰는 코드이다
사용자가 뭐라 메시지를 치면
`await message.channel.send()`로 봇이 반응한다
`await message.channel.send("안녕하세요!")` <= 이렇게 문자열과 문자를 넣어 봇이 메시지를 보낼수 있게 한다
이 코드는 봇이 메시지를 보낸다
예시:
```
if message.content == "!안녕" or message.content == "!안녕하세요":
    await message.channel.send("안녕하세요!")
```
# 다른 기능 설명
```
@bot.command(name="delete")
@commands.has_role("MessageManager")
async def delete_message(ctx):
    await ctx.channel.purge(limit=None)

@bot.event
async def on_command_error(ctx, error):
    pprint("Command error")
```
# 이 코드는 메시지 삭제 기능이다


