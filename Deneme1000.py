import discord
import os
import random

Faktöriyel = 1

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def FaktöriyelBulma(ctx, sayi):
    if sayi == 5:
        await ctx.send("do")
    elif sayi != 5 :
        await ctx.send("yANLIŞ")
    print(sayi)
    




bot.run('MTEyNzY0MDk5NjY4Mzk3MjcyOA.Gtran9.EskiBvFKhARfdUDnh6cqNBK4pwokV0h0uHFqdw') 