from random_words import RandomWords
import discord
import requests
from discord.ext import commands
import asyncio


def setup(client):
    client.add_cog(hangman(client))


class hangman(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['hm'])
    async def hangman(self, ctx):
        rw = RandomWords()
        word = rw.random_word()
        if len(word) <= 4:
            rw = RandomWords()
            word = rw.random_word()
        vowels = ['a', 'e', 'i', 'o', 'u']
        if word[-1] == 's' and word[-2] == 'e' and word[-3] not in vowels:
            word = word[:len(word)-3]
        elif word[-1] == 's' and word[-2] != 'e':
            word = word[: len(word)-2]
        l = []
        for i in range(0, len(word)):
            l.append(word[i])

        guessed_letters = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        send = ''
        for i in range(0, len(word)):
            send = send + ':brown_square: '
        
        guess0 = fr"""```    _____                   
    |     |                 
    |                       
    |                       
    |                       
    |                       
____|_____________          
```"""
        guess1 = fr"""```    _____                   
    |     |                 
    |     @                 
    |                       
    |                       
    |                       
____|_____________          
```"""
        guess2 = fr"""```    _____                   
    |     |                 
    |     @                 
    |     |                 
    |     |                 
    |                       
____|_____________          
```"""
        guess3 = fr"""```    _____                   
    |     |                 
    |     @                 
    |    \|                 
    |     |                 
    |                       
____|_____________          
```"""
        guess4 = fr"""```    _____                   
    |     |                 
    |     @                 
    |    \|/                
    |     |                 
    |                       
____|_____________          
```"""
        guess5 = fr"""```    _____                   
    |     |                 
    |     @                 
    |    \|/                
    |     |                 
    |    /                  
____|_____________          
```"""
        guess6 = fr"""```    _____                   
    |     |                 
    |     @                 
    |    \|/                
    |     |                 
    |    / \                
____|_____________          
```"""
        guess = 0
        guess_list = [guess0, guess1, guess2, guess3, guess4, guess5, guess6]
        guessmessage = ["Looks like you haven't started the hanging process yet.", "Ooo, your first mistake.", "Ouch, you second mistake", "Poor guy, your third mistake", "Damn, your 4th mistake.", "Almost dead. . .", "Sorry, looks like you've been hanged."]

        embed = discord.Embed(
            title = 'Hangman',
            description = 'Please type a letter in the chat.',
            color = ctx.author.color
        )
        embed.add_field(name = send, value = 'I wonder what this word is.', inline = False)
        embed.add_field(name = guess_list[guess], value = guessmessage[guess], inline = False)
        embed.add_field(name = 'Guessed letters:', value = guessed_letters, inline = False)
        embed2 = embed
        info = await ctx.send(embed = embed)

        while True:
            def check(m):
                return m.channel == ctx.channel and m.content.lower() in letters
            try:
                msg = await self.client.wait_for('message', timeout = 25.0, check = check)
                
            except asyncio.TimeoutError:
                await ctx.send('Timed out.')
                return
            await msg.delete()
            if msg.content in l:
                if msg.content not in guessed_letters:
                    guessed_letters.append(msg.content)
                    letters.remove(msg.content)
                    for j in range(0, len(word)):
                        if word[j] == msg.content:
                            sendsplit = send.split()
                            sendsplit[j] = msg.content 
                            send = ' '.join(sendsplit)
                
    
            else:
                if msg.content.lower() not in guessed_letters:
                    guess += 1
                    guessed_letters.append(msg.content.lower())

            
            if guess == 6:
                send = ''
                for i in range(0, len(word)):
                    send = send + word[i] + ' '
                
                for i in guessed_letters:
                    if i in l:
                        guessed_letters.remove(i)
                embed2.clear_fields()
                embed2.add_field(name = send, value = 'Oh, so thats what\n this word is.', inline = False)
                embed2.add_field(name = guess_list[guess], value = guessmessage[guess], inline = False)
                embed2.add_field(name = 'Incorrect letters:', value = guessed_letters, inline = False)
                await info.edit(embed = embed2)
                return
            if ''.join(send.split()) == word:
                for i in guessed_letters:
                    if i in l:
                        guessed_letters.remove(i)
                embed2.clear_fields()
                embed2.add_field(name = send, value = 'Congratulations! You guessed the word!', inline = False)
                embed2.add_field(name = guess_list[guess], value = 'Good job!', inline = False)
                embed2.add_field(name = 'Incorrect letters:', value = guessed_letters, inline = False)
                await info.edit(embed = embed2)
                return
             
            embed2.clear_fields()
            embed2.add_field(name = send, value = 'What could this word be?', inline = False)
            embed2.add_field(name = guess_list[guess], value = guessmessage[guess], inline = False)
            embed2.add_field(name = 'Guessed letters:', value = guessed_letters, inline = False)
            await info.edit(embed = embed2)

            
            
