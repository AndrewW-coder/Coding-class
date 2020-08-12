import discord
import math
from math import sqrt
from discord.ext import commands
import random
import os
import time


#prefix
client = commands.Bot(command_prefix = ('yeet.', 'yeet ', 't.'))
#IDK
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')
#startup
@client.event
async def on_ready():
    print("bot has connected to discord")
    game = discord.Game('Minecraft')
    await client.change_presence(status=discord.Status.idle, activity=game)

#commands






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



l = ['It is certain',
 'It is decidedly so', 
 'Outlook good', 
 'Ask again later, you noob',
 'Better not tell you now', 
 "Don't count on it", 
 'my sources say no', 
 'Very doubtful',
 'What type of question is that?!',
 'How do you not know the answer?!',
 'Bruh']
n = random.randint(0, len(l) - 1)
@client.command()
async def eightball(ctx):
    n = random.randint(0, len(l) - 1)
    await ctx.send(l[n]) 
    
    

c = ['Heads', 'Tails']
r = random.randint(0, len(l) - 1)
@client.command()
async def coinflip(ctx):
    await ctx.send(c[r])

@client.command()
async def spam(ctx, a:str, b:int):
    await ctx.send((a + '\n') * b) 

@client.command(pass_context=True)
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')

@client.command(pass_context=True)
async def p(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  {int(ping)}ms")
    print(f'Ping {int(ping)}ms')

@client.command()
async def pl(ctx):
    if ping or p < ping:
        d = ping
    embed = discord.Embed(
        title = "Ping Leaderboard",
        description = f'Lowest ping: {d}',
        color = discord.Color.from_rgb(r, g, b)
    )
    await ctx.send(embed = embed)


client.run('NzMxOTY0MDM0ODY1Mjk5NTM3.XwtsoQ.2MNOPAWPZWoSr-oorbTIxX4rmxg')