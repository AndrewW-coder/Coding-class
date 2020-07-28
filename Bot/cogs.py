import discord
from discord.ext import commands


class cogs(commands.Cog):

    @commands.command()
    async def trivia(self, ctx):



def setup(client):
    client.add_cog(cogs(client))