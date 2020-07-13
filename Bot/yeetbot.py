import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = 'yeet.')

@client.event
async def on_ready():
    print("bot has connected to discord")

@client.command()
async def song(ctx):
    await ctx.send("creeper, awwwwm mannnn")

@client.command()
async def hi(ctx):
    await ctx.send("hello")

@client.command()
async def coinflip(ctx):
    await ctx.send(
x = randint(1, 2)
if x == 1:
    print('Heads')
else print('Tails')
    )





client.run('NzMxOTY0MDM0ODY1Mjk5NTM3.XwuDQA.UYe89ocatn6uhJ3Jkl_orQBYBN0')