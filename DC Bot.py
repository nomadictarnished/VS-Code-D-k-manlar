import discord
import os
import random
import requests

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


print(os.listdir('resim'))
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def mem(ctx):
    çekici = random.choice(os.listdir('resim'))
    with open(f'resim/{çekici}', 'rb') as f:
        resim = discord.File(f)
    
    await ctx.send(file=resim) 

    if çekici == '30.jpg':
        with open(f'resim/a.jpg','rb') as a:
            resim   = discord.File(a)
            await ctx.send(file=resim)
    elif çekici == 'b.jpg':
        with open(f'resim/a.jpg','rb') as a:
            resim   = discord.File(a)
            await ctx.send(file=resim)

def çek():
    çekici = random.choice(os.listdir('resim'))
    for i in range(1,10):
        çekici * i
        return çekici
    print(i)

    
            

bot.run("MTEyNzY0MDk5NjY4Mzk3MjcyOA.GvjP9O.5a-w0b9Wo8KNTzZyL9t2b6JLRamF9ZzM8wKLAY")