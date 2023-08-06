import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def add(ctx, sayi):
       await ctx.send("yAZDIĞIN SAYI: {0}".format(sayi))

bot.run("MTEyNzY0MDk5NjY4Mzk3MjcyOA.GOkkez.20Of2OGk3jTW0jMc42SsAIPNRr-KL_wrzmmYuY")