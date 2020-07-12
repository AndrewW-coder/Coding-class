import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'yeet.')

@client.event
async def on_ready():
    print("bot has connected to discord")

@client.command()
async def hi(ctx):
    await ctx.send(f"hello, {ctx.author.display_name}")

@client.command()
async def fruit(ctx):
    await ctx.send("I like to eat, eat, eat, apples and bananas.")

@client.command()
async def song(ctx):
    await ctx.send("Creeper, aaaaaaaaaaaaaaaaaaaaaaaawwwwwwwwwwwwwwwwwwwwww mmmmmmaaaaaaaaannnnnnnn.")

@client.command()
async def server(ctx):
    await ctx.send(f"This is {ctx.guild.name}")

   

client.run('NzMxOTY0MDM0ODY1Mjk5NTM3.Xwtsyg.Q4bcut0VYrulJvwvWp_xwp_mJxA')