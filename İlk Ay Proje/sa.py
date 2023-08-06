import discord
import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def FaktöriyelBulma(sayi):
        Faktöriyel = 1
        for i in range(1,Faktöriyel+ 1):
            Faktöriyel *= i
            return Faktöriyel

bot.run("MTEyNzY0MDk5NjY4Mzk3MjcyOA.GvjP9O.5a-w0b9Wo8KNTzZyL9t2b6JLRamF9ZzM8wKLAY")

















