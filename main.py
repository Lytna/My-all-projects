from aiohttp import request
import discord
from discord.ext import commands
import fonk
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Çalışır durumda!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')
    await ctx.send("Merhaba discorda hoş geldiniz.")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx):
    await ctx.send(f'İyi ki geldin {ctx.author}')

@bot.command()
async def topla(ctx, s1 = 0, s2 = 0):
    await ctx.send(f"{s1}+{s2} = {s1+s2}")

@bot.command()
async def toplama(ctx,*args):
    try:
        #toplam = sum(float(arg) for arg in args)
        a = 0
        for i in args:
            a+=float(i)
        await ctx.send(f"Cevap {a}")
    except:
        await ctx.send("Sayi girmeniz lazım. ")

@bot.command()
async def ortalama(ctx,*args):
    try:
        a = 0
        b = len(args)
        for i in args:
            a+=(float(i)/b)
        await ctx.send(f"Cevap {a}")
    except:
        await ctx.send("Sayi girmeniz lazım. ")



    
@bot.command()
async def çarp(ctx, s1 = 1, s2 = 1):
    await ctx.send(f"{s1}x{s2} = {s1*s2}")

@bot.command()
async def böl(ctx, s1 = 1, s2 = 1):
    await ctx.send(f"{s1}÷{s2} = {s1/s2}")

@bot.command()
async def çıkar(ctx, s1 = 0, s2 = 0):
    await ctx.send(f"{s1}-{s2} = {s1-s2}")
        
@bot.command()
async def olustur(ctx,s=1):
    await ctx.send(fonk.fonksiyon(s))

@bot.command()
async def oyun(ctx,a):
    if a.lower() not in ["yazı", "tura"]:
        await ctx.send("Lütfen 'yazı' veya 'tura' olarak geçerli bir tahmin yapın.")
        return 
    sonuc = "yazı" if random.randint(1, 2) == 1 else "tura"
    if a.lower() == sonuc:
        await ctx.send("Doğru tahmin")
    else:
        await ctx.send("Yanlış tahmin")


@bot.command()
async def mem(ctx):
    
    memrandom = random.choice(os.listdir('resimler'))
    with open(f'resimler/{memrandom}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('ordek')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('utku')
async def dog(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_random_pokemon_image_url():
    base_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_id = str(random.randint(1, 807))  # Toplamda 807 Pokemon var, bu değeri isteğe bağlı değiştirebilirsin
    url = base_url + pokemon_id
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['sprites']['front_default']
        
        return image_url
    else:
        return None

@bot.command('poke')
async def pokemon(ctx):
    '''pokemon komutunu çağırdığımızda, get_random_pokemon_image_url fonksiyonunu çağırır.'''
    image_url = get_random_pokemon_image_url()

    if image_url:
        await ctx.send(image_url)



@bot.command()
async def tahminoyunu(ctx,s1=0 , s2=100):
    a = random.randint(s1,s2)
    await ctx.send("Başlayabilirsin")
    b = 8
    while b > 0:
        tahmin_mesaji = await bot.wait_for("message", check=lambda m: m.author == ctx.author)     
        kullanici_tahmini = tahmin_mesaji.content
        try:
            kullanici_tahmini = int(kullanici_tahmini)

        except:
            await ctx.send("Sayı girmeniz lazım")
            continue
        
        b-=1     
        if b > 0:
            if kullanici_tahmini == a:
                await ctx.send("Doğru tahmin!")
                break
            elif kullanici_tahmini < a:           
                await ctx.send("Daha büyük bir tahminde bulun")
                await ctx.send(f"{b} Hakkınız kaldı")


            else:
                await ctx.send("Daha küçük bir tahminde bulun")    
                await ctx.send(f"{b} Hakkınız kaldı")

    else:
        await ctx.send("Hakkınız kalmadı")

        
@bot.command()
async def faktoryel(ctx,s1= 1):
    a = 1
    for i in range(1,s1+1): 
        a*=float(i)
    await ctx.send(a)
    





    


bot.run("YOUR TOKEN :) ")