import discord
import requests
from discord.ext import commands
import aiohttp


def setup(client):
    client.add_cog(Joke(client))


class Joke(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.headers = {
            "User-Agent": "yeetbot",
            "Accept": "text/plain",
        }
    @commands.command(aliases = ["j"])
    async def joke(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://icanhazdadjoke.com', headers = self.headers) as r:
                if r.status == 200:
                    result = await r.text()
                    result = result.encode("utf-8").decode("utf-8")
                    embed = discord.Embed(
                        title = ':rofl: funniez jokes :rofl:',
                        description = f"{result}",
                        colour = ctx.author.color                     
                    )
                    await ctx.send(embed=embed)   
    
