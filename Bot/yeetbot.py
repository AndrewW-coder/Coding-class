import discord
import math
from math import sqrt
from discord.ext import commands
import random
#prefix
client = commands.Bot(command_prefix = ('yeet.', 'yeet '))
#startup
@client.event
async def on_ready():
    print("bot has connected to discord")
    game = discord.Game('Valorant sucks, play minecraft')
    await client.change_presence(status=discord.Status.idle, activity=game)

#commands

#songs
@client.command()
async def revenge(ctx):
    await ctx.send("creeper, awwwwm mannnn")

@client.command()
async def diggy_hole(ctx):
    await ctx.send("I am a dwarf and I'm digging a hole. Diggy diggy hole. Diggy diggy hole.")

@client.command()
async def TNT(ctx):
    await ctx.send("I came to dig dig dig dig. I'll build a city oh so big big big big.")


@client.command()
async def songs(ctx):
    await ctx.send('yeet.diggy_hole, yeet.TNT, yeet.revenge')
#greet
@client.command()
async def hi(ctx):
    await ctx.send("hello")
#game
@client.command()
async def valorant(ctx):
    await ctx.send("👎")

async def minecraft(ctx):
    await ctx.send(":thumbsup:")

async def games(ctx):
    await ctx.send("yeet.minecraft, yeet.valorant")

@client.command()
async def rickroll(ctx):
    await ctx.send("https://tenor.com/view/rickroll-dance-funny-you-music-gif-7755460")

#maths
@client.command()
async def add(ctx, a:int, b:int):
    await ctx.send(a + b)

@client.command()
async def multiply(ctx, a:int, b:int):
    await ctx.send(a * b)

@client.command()
async def subtract(ctx, a:int, b:int):
    await ctx.send(a - b)

@client.command()
async def divide(ctx, a:int, b:int):
    await ctx.send(a / b)

@client.command()
async def squarert(ctx, a:int):
    await ctx.send(sqrt(a))

@client.command()
async def square(ctx, a:int):
    await ctx.send(a ** 2)

@client.command()
async def maths(ctx):
    await ctx.send('yeet.add, yeet.subtract, yeet.multiply, yeet.subtract, yeet.squarert, yeet.square')

#fun
@client.command()
async def kill(ctx, a:str):
    await ctx.send(a + ' has been eliminated.')

@client.command()
async def revive(ctx, a:str):
    await ctx.send(a + ' has been revived.')

@client.command()
async def pwnnoob(ctx, a:str):
    await ctx.send(a + ' has been killed. What a noob.')
@client.command()
async def life(ctx):
    await ctx.send("yeet.kill, yeet.revive, yeet.pwnnoob")

@client.command()
async def embed1(ctx):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    embed = discord.Embed(
        title = "Weird stuff",
        color = discord.Color.from_rgb(r, g, b),
        description = 'Testing.'
    )
    embed.add_field(name = 'Bananas', value = 'They taste like bananas.', inline = False)
    embed.add_field(name = 'Apples', value = 'They taste like apples', inline = False)
    embed.set_image(url = 'https://media.discordapp.net/attachments/731981056701497354/734487509194506412/Rick-Roll3.png?width=770&height=679')
    embed.set_footer(text = 'This is a rickroll, beware!')
    await ctx.send(embed = embed)

@client.command()
async def embed2(ctx):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    embed = discord.Embed(
        title = "How to cook food",
        color = discord.Color.from_rgb(r, g, b),
        description = "Pick up a pan. Throw it at a wall since you can't cook. Order a pizza."
    )
    embed.add_field(name = 'Bananas', value = 'They taste like Bananas.', inline = False)
    embed.add_field(name = 'Apples', value = 'They taste like apples', inline = False)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/731981056701497354/734855467393613996/3566af35b24fec468260f99c54a10505a8ed332br1-1006-998v2_uhq.png')
    embed.set_footer(text = 'The future!')
    await ctx.send(embed = embed)




#shots
# @client.command()
# async def headshot(ctx, a:str):
#     await ctx.send(a + ' has been headshot and has been eliminated.')

# @client.command()
# async def swagshot(ctx, a:str):
#     await ctx.send(a + ' has been 360 no-scoped. They should be embarrased')

# @client.command()
# async def dankshot(ctx, a:str):
#     await ctx.send(a + ' has been dankified so hard, they died')

# @client.command()
# async def shots(ctx):
#     await ctx.send('yeet.swagshot, yeet.headshot, yeet.dankshot')

#guns
# @client.command()
# async def use_shotgun(ctx):
#     await ctx.send('You are using a shotgun')

# @client.command()
# async def use_sniper_rifle(ctx):
#     await ctx.send('You are using a sniper rifle')

# @client.command()
# async def use_AR(ctx):
#     await ctx.send('You are using a AR')

# @client.command()
# async def guns(ctx):
#     await ctx.send('yeet.use_sniper_rifle, yeet.use_shotgun, yeet.use_AR')

l = ['It is certain', 'It is decidedly so', 'Yes', 'Outlook good', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'No', "Don't count on it", 'my sources say no', 'Very doubtful']
n = random.randint(0, len(l) - 1)
@client.command()
async def eightball(ctx):
    await ctx.send(l[n])

c = ['Heads', 'Tails']
r = random.randint(0, len(l) - 1)
@client.command()
async def coinflip(ctx):
    await ctx.send(c[r])

@client.command()
async def commands(ctx):
    await ctx.send("yeet.hi, yeet.song, yeet.games, yeet.rickroll, yeet.maths, yeet.shots, yeet.guns, yeet.eightball, yeet.life")
client.run('NzMxOTY0MDM0ODY1Mjk5NTM3.Xwx6Vw.waQZYsmLL8WNHOR4xnF13n_LTLM')