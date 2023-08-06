import discord

import infdict
import random


from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)
a = infdict.hayvanlar
b = infdict.bitkiler
c = infdict.su
d = infdict.hava
@bot.event
async def on_ready():
    print(f'Selamın Aleyküm {bot.user} Kardeşim ')

@bot.command()
async def inf(ctx, param):
    
    seçimha = random.choice(d)
    seçims = random.choice(c)
    seçimb = random.choice(b)
    seçimh = random.choice(a)
    if param == "hayvanlar":
         await ctx.send(seçimh)
    elif param == "bitkiler":
         await ctx.send(seçimb)
    elif param == "su":
         await ctx.send(seçims)
    elif param == "hava":
         await ctx.send(seçimha)
    
    else :
         await ctx.send("Komutlar: inf hayvanlar, inf bitkiler, inf su, inf hava")

@bot.command()
async def yardım(ctx):
     await ctx.send("Geçerli Komutları: inf hayvanlar, inf bitkiler, inf hava, inf su")
    
    

bot.run('MTEyNzY0MDk5NjY4Mzk3MjcyOA.GDFfSN.4kwVh2_Ykwti-ufex7dHoqtBfK9n0spDnfEHK0') 