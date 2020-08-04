import discord
import requests
from discord.ext import commands
import os
import random
import html



class games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trivia(self, ctx):
        data = requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()
        results = data['results'][0]
        embed = discord.Embed(
            title = ":question: Trivia",
            description = f"Category: {results['category']} | Difficulty: {results['difficulty'].capitalize()}",
            color = ctx.author.color
        )
        pos = random.randint(0, 3)
        if pos == 3:
            answers = results['incorrect_answers'] + [results['correct_answer']]
        else:
            answers = results['incorrect_answers'][0:pos] + [results['correct_answer']] + results['incorrect_answers'][pos:]
        embed.add_field(name = html.unescape(results['question']), value = "answers here")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(games(client))