import discord


from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix ='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Kütle_İndeks(ctx, Kilo, Boy):
    await ctx.send("Kilonuzu ve Boyunuzu sırasıyla aralarında boşluk olacak şekilde yazın:")
