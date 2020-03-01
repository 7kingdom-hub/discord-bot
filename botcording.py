pip install discord
pip install asyncio
import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("'킹다리는 인정이지!' 라고 발언")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
        
    if message.content.startswith("!사다리"):
        line_ = ['탑', '정글', '미드', '원딜', '서폿']
        a = random.choice(line_)
        b = random.choice(line_)
        c = random.choice(line_)
        d = random.choice(line_)
        e = random.choice(line_)

        while b == a:
            b = random.choice(line_)
        while c == a or c == b:
            c = random.choice(line_)
        while d == a or d == b or d == c:
            d = random.choice(line_)
        while e == a or e == b or e == c or e == d:
            e = random.choice(line_)

        A = "1번 =" + a
        B = "2번 =" + b
        C = "3번 =" + c
        D = "4번 =" + d
        E = "5번 =" + e
        await message.channel.send(A)
        await message.channel.send(B)
        await message.channel.send(C)
        await message.channel.send(D)
        await message.channel.send(E)
     


client.run("NjgzNjkzMjY2Mjc2OTc0NjEy.XlvRVg.XWYYCT5Zl2HhWB5S4_jpwfb23gA")
