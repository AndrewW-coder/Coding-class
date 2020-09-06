import discord
import requests
from discord.ext import commands
# import wordsapiv1

def setup(client):
    client.add_cog(Definition(client))

class Definition(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['def'])
    async def definition(self, ctx, *, word):  
        url = (f'https://wordsapiv1.p.mashape.com/words/{word}')
        response = requests.get(url)
        data = response.json()
        print(data)