import discord
import requests
from discord.ext import commands
import os
import random
import html
import asyncio
import aiohttp

def setup(client):
    client.add_cog(joke(client))


class joke(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases = ["j"])
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com') as a:
                if a.status == 200:r
                    result = result.encode("utf-8").decode("utf-8")ar
                    embed = discord.Embed(
                        title = ':rofl:',
                        description = f"{result}",
                        colour = ctx.author.color                     
                    )
                    await ctx.send(embed=embed)
def setup(client):
    client.add_cog(joke(client))