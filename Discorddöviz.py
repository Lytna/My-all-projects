import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Çalışır durumda!')


def doviz_kuru(s1,s2):
    url = 'https://api.currencyfreaks.com/latest?apikey=40ca016a37054e2393b0983dca74e83d&base='
    response = requests.get(url)
    data = response.json()
    kur1 = data["rates"][f"{s1}"]
    kur2 = data["rates"][f"{s2}"]
    return kur1,kur2

@bot.command()
async def kur(ctx,s1,s2):
    cevap = doviz_kuru(s1,s2)
    x = float(cevap[1])/float(cevap[0])
    await ctx.send(round(x,2))


bot.run('YOUR TOKEN : ) ')
