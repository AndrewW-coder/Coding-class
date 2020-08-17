import discord
from discord.ext import commands
import asyncio
def setup(client):
    client.add_cog(change_color(client))

class change_color(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def change_color(self, ctx):
        l = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        await ctx.send('The colors you can change to are: ')
        await ctx.send(', '.join(l))
        # r = 0
        # b = 0
        # g = 0
        def check(m):
            return m.channel == ctx.channel and m.content.lower() in l
        try:
            msg = await self.client.wait_for('message', timeout = 20.0, check = check)
            
        except asyncio.TimeoutError:
            return
        r1 = 0
        g1 = 0
        b1 = 0
        if msg.content.lower == 'red':
            r1 = 255
            g1 = 1
            b1 = 1
        if msg.content.lower == 'orange':
            r1 = 255
            g1 = 98
            b1 = 1
        if msg.content.lower == 'yellow':
            r1 = 255
            g1 = 226
            b1 = 1
        if msg.content.lower == 'green':
            r1 = 1
            g1 = 255
            b1 = 1
        if msg.content.lower == 'blue':
            r1 = 1
            g1 = 1
            b1 = 255
        embed = discord.Embed(
            title = 'You have successfully changed your color!',
            desription = '',
            color = discord.Color.from_rgb(r1, g1, b1)
        )
        await ctx.send(embed = embed)
        
