import discord
import os
import random
import requests


from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

def resim_çek():
    url  = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = resim_çek()
    await ctx.send(image_url)