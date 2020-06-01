import asyncio
import discord
from discord.utils import get

app = discord.Client()

token = "NzA3NTc3OTM2MTY0NjgzODI3.XtROXg.xQXRk8GSsaq1qPhd-SKycnTTqLo"
calcResult = 0

@app.event
async def on_ready():
    print("다음계정에 로그인을 시도합니다! : ")
    print("국병봇")
    print(app.user.id)
    print("로그인 완료!")
    game = discord.Game("개발중")
    await app.change_presence(status=discord.Status.idle, activity=game) 

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!핵제보":
        await message.channel.send("테스트구문 실행완료!")
    if message.content.startswith("국병님 1부터5까지 세줘요"):
        for x in range(5):
            await message.channel.send(x+1)
    if message.content.startswith("!테스트"):
        id = message.author.id
        await message.channel.send("<@" + str(id) + ">, 테스트완료 오류 없음")
    if message.content.startswith('!도움말'):
        embed = discord.Embed(title="국병봇 명령어", description="아래의 명령어를 확인하고 입력해 주세요!", color=0x00ff56)
        embed.set_author(name="국병봇 by GM국병", url="https://cdn.discordapp.com/attachments/538324804584079360/707791264766099526/JPEG_20191103_134708.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/538324804584079360/707791264766099526/JPEG_20191103_134708.png")
        embed.add_field(name="!핵신고", value="핵유저 제보를 하실때 사용해 주세요", inline=False)
        embed.set_footer(text="국병봇은 준루트서버에서만 사용가능합니다")
        await message.channel.send(embed=embed)
    if message.content.startswith("!핵신고"):
        me = get(message.guild.members, id=479999678319165441)
        channel = await me.create_dm()
        await channel.send("핵신고가 접수되었습니다.")
        await message.channel.send(f"{message.author.mention}님,정상적으로 접수되었습니다 제보 감사합니다.")
    if message.content.startswith("!건의"):
        me = get(message.guild.members, id=479999678319165441)
        channel = await me.create_dm()
        await channel.send("건의가 접수되었습니다.")
        await message.channel.send(f"{message.author.mention}님,곧 개인적으로 연락을 드릴겁니다 감사합니다.")
    if message.content.startswith("!규칙"):
        channel = await message.author.create_dm()
        await message.author.create_dm()
        await channel.send("규칙 내용")
    if message.content.startswith("!운영자 신청"):
        channel = await message.author.create_dm()
        await message.author.create_dm()
        await channel.send(f"{message.author.mention}현재 운영자신청은 https://forms.gle/F89f1weHbhgJyyz39 에서 제출해주세요")
    if message.content.startswith("!규칙"):
        await message.author.send('안녕')


app.run(')