import discord

client = discord.Client()

token = "ODAwMjkzMTI4Nzc0NjE1MDYy.YAQBDg.F65dbdnAgkRhP11wUl6gbRuJFqw"

@client.event
async def on_ready():
    print(client.user.name)
    print("재플이 준비 완료!")
    game = discord.Game("GApple님을 찬양하라!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "재플아":
        await message.channel.send("**하이!**")
    if message.content == "재플아 뭐하니":
        await message.channel.send("**알아서 뭐하게**")
    if message.content == "재플아 안녕":
        await message.channel.send("**하이!**")
    if message.content == "재플아 ㅋㅋ":
        await message.channel.send("**미친건가...**")
    if message.content == "재플아 ㅎㅇ":
        await message.channel.send("**ㅎㅇ**")
    if message.content == "재플아 바이":
        await message.channel.send("**ㅇㅇ ㅂㅇ**")
    if message.content == "재플아 ㅂㅇ":
        await message.channel.send("**ㅂㅇ**")
    if message.content == "재플아 낚시":
        await message.channel.send("**난 이프가 아니라구**")
    if message.content == "ㅅㅂ":
        await message.channel.send("**감히 ㅅㅂ이라고 하다니!**")
    if message.content == "재플아 야":
        await message.channel.send("**뭐**")
    if message.content == "재플아 재플":
        await message.channel.send("**뭐 왜**")
    if message.content == "재플아 굿나잇":
        await message.channel.send("**난 안잠**")
    if message.content == "재플아 잘자":
        await message.channel.send("**시러 난 안잘거야**")
    if message.content == "재플아 ㅂㅇㄹ":
        await message.channel.send("**보이루!**")
    if message.content == "재플아 보이루":
        await message.channel.send("**ㅂㅇㄹ**")
    if message.content == "시발":
        await message.channel.send("**감히 시발이라고 하다니!**")
    if message.content == "ㅁㅊ":
        await message.channel.send("**감히 ㅁㅊ이라고 하다니!**")
    if message.content == "미친":
        await message.channel.send("**감히 미친이라고 하다니!**")
    if message.content == "ㅂㅅ":
        await message.channel.send("**감히 ㅂㅅ이라고 하다니!**")
    if message.content == "병신":
        await message.channel.send("**감히 병신이라고 하다니!**")
    if message.content == "ㅄ":
        await message.channel.send("**감히 ㅄ이라고 하다니!**")
    if message.content == "ㅅㅅ":
        await message.channel.send("**감히 ㅅㅅ라고 하다니!**")
    if message.content == "섹스":
        await message.channel.send("**감히 섹스라고 하다니!**")
    if message.content == "바보":
        await message.channel.send("**감히 바보이라고 하다니!**")
    if message.content == "재플아 너":
        await message.channel.send("**뭐**")
    if message.content == "재플아 날씨":
        await message.channel.send("**난 날씨 상관 없음**")
    if message.content == "재플아 시간":
        await message.channel.send("**몰라**")
    if message.content == "재플아 앙":
        await message.channel.send("**기모띠**")
    if message.content == "재플아 뷁":
        await message.channel.send("**쀍쮉뛝쒥뭵뉅웱뤩**")
    if message.content == "재플아 하하하":
        await message.channel.send("**미친거군**")
    if message.content == "재플아 나가":
        await message.channel.send("**너나 꺼져**")
    if message.content == "재플아 꺼져":
        await message.channel.send("**카악 퉤!**")
    if message.content == "재플아 도배":
        await message.channel.send("**도배도배**")



client.run(token)
