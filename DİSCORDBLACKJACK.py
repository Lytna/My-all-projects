import datetime
import discord
from discord.ext import commands
from discord.ui import Button, View
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} Çalışır durumda!')


def kart_degeri(kart):
    if kart in ['J', 'Q', 'K']:
        return 10
    elif kart == 'A':
        return 11
    else:
        return int(kart)

def kart_destesi_olustur():
    destedeck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(destedeck)
    return destedeck

def oyuncu_ve_krupiyeyi_baslat(deste):
    return [deste.pop(), deste.pop()], [deste.pop(), deste.pop()]

def oyuncu_skoru(kartlar):
    skor = sum([kart_degeri(kart) for kart in kartlar])
    as_sayisi = kartlar.count('A')
    
    while as_sayisi > 0 and skor > 21:
        skor -= 10
        as_sayisi -= 1
    
    return skor

def blackjack_kontrol(kartlar):
    return len(kartlar) == 2 and oyuncu_skoru(kartlar) == 21

def kazanan_kontrolu(oyuncu_skoru, krupiye_skoru):
    if oyuncu_skoru > 21:
        return "Krupiye kazandı. Oyuncu battı!"
    elif krupiye_skoru > 21:
        return "Oyuncu kazandı. Krupiye battı!"
    elif oyuncu_skoru == krupiye_skoru:
        return "Berabere! Skorlar eşit."
    elif oyuncu_skoru > krupiye_skoru:
        return "Oyuncu kazandı!"
    else:
        return "Krupiye kazandı!"

def baskent_bul(ulke):
    baskentler = {
    'türkiye': 'Ankara',
    'fransa': 'Paris',
    'almanya': 'Berlin',
    "ispanya": "Madrid"
    }


@bot.command()
async def denemeblackjack(ctx):
    destedeck = kart_destesi_olustur()
    oyuncu_kartlari, krupiye_kartlari = oyuncu_ve_krupiyeyi_baslat(destedeck)

    while True:
        await ctx.send(f"Oyuncu Kartları: {oyuncu_kartlari}, Toplam Skor: {oyuncu_skoru(oyuncu_kartlari)}")
        await ctx.send(f"Krupiye'nin Gösterilen Kartı: {krupiye_kartlari[0]}")

        if blackjack_kontrol(oyuncu_kartlari):
            await ctx.send("Blackjack! Oyuncu kazandı.")
            break

        # Evet/Hayır butonları oluştur
        buttons = [
            discord.ui.Button(style=discord.ButtonStyle.green, label="Evet"),
            discord.ui.Button(style=discord.ButtonStyle.red, label="Hayır")
        ]
        view = discord.ui.View()
        view.add_item(buttons[0])
        view.add_item(buttons[1])

        await ctx.send("Kart çekilsin mi?", view=view)

        # Kullanıcının buton seçimini bekleyin
        interaction, _ = await bot.wait_for('button_click', check=lambda i: i.user.id == ctx.author.id)

        if interaction.component.label == "Evet":
            oyuncu_kartlari.append(destedeck.pop())
        else:
            break

    while oyuncu_skoru(krupiye_kartlari) < 17:
        krupiye_kartlari.append(destedeck.pop())

    await ctx.send(f"\nOyuncu Kartları: {oyuncu_kartlari}, Toplam Skor: {oyuncu_skoru(oyuncu_kartlari)}")
    await ctx.send(f"Krupiye Kartları: {krupiye_kartlari}, Toplam Skor: {oyuncu_skoru(krupiye_kartlari)}")

    await ctx.send(kazanan_kontrolu(oyuncu_skoru(oyuncu_kartlari), oyuncu_skoru(krupiye_kartlari)))




@bot.command()
async def basit_embed(ctx):
    embed = discord.Embed(
        title="Basit Embed",
        description="Bu bir basit embed örneğidir.",
        color=0x3498db  # Mavi renk
    )
    
    await ctx.send(embed=embed)


@bot.command()
async def baskent(ctx, ulke):
    response = baskent_bul(ulke)
    embed = discord.Embed(title=f"{ulke.capitalize()}'in Başkenti", color=0x0000FF)
    embed.add_field(name="Ülke", value=ulke.capitalize(), inline=False)
    embed.add_field(name="Başkent", value=response, inline=False)
    türkiye = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgdMrNuqW05SYQJiXP8x0wrGsHrI_0UhLyb0WCoMiOHISttbkuONm4W5wOpUgamAalTbw&usqp=CAU"
    fransa = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB0vLtSAol6z_zMw90LNaH6F_tZjCDUU8RLckhmIe3TrweENyqUPAyY9lITvW0vG0JIQY&usqp=CAU"
    if ulke == "türkiye":
        embed.set_image(url=türkiye)
    elif ulke == "fransa":
        embed.set_image(url=fransa)
    await ctx.send(embed=embed)

@bot.command()
async def denemeembed(ctx):
    embed = discord.Embed(title="Başlık", description="Açıklama", color=0x00ff00)
    embed.set_image(url="https://cdn.mos.cms.futurecdn.net/8KyCYsto2PoN2r23PxDG27.jpg")
    embed.set_thumbnail(url="https://cdn.mos.cms.futurecdn.net/8KyCYsto2PoN2r23PxDG27.jpg")
    embed.set_footer(text="Altbaşlık", icon_url="https://cdn.mos.cms.futurecdn.net/8KyCYsto2PoN2r23PxDG27.jpg")
    embed.add_field(name="Alan Adı", value="Alan Değeri", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.url = "https://www.youtube.com/channel/UChqLHxYnIAH4iY1Vlu9MXJg"
    embed.set_author(name="Yazar Adı", icon_url="https://www.youtube.com/channel/UChqLHxYnIAH4iY1Vlu9MXJg")
    embed.add_field(name="Markdown Tablo", value="```python\nprint('Merhaba')\n```")
    embed.add_field(name="\u200b", value="\u200b")

    await ctx.send(embed=embed)

@bot.command()
async def blackjack(ctx):
    destedeck = kart_destesi_olustur()
    oyuncu_kartlari, krupiye_kartlari = oyuncu_ve_krupiyeyi_baslat(destedeck)

    while True:
        await ctx.send(f"Oyuncu Kartları: {oyuncu_kartlari}, Toplam Skor: {oyuncu_skoru(oyuncu_kartlari)}")
        await ctx.send(f"Krupiye'nin Gösterilen Kartı: {krupiye_kartlari[0]}")

        if blackjack_kontrol(oyuncu_kartlari):
            await ctx.send("Blackjack! Oyuncu kazandı.")
            break

        response = await bot.wait_for('message')
        if response.author == ctx.author and response.content.lower() == 'evet':
            oyuncu_kartlari.append(destedeck.pop())
        else:
            break

    while oyuncu_skoru(krupiye_kartlari) < 17:
        krupiye_kartlari.append(destedeck.pop())

    await ctx.send(f"\nOyuncu Kartları: {oyuncu_kartlari}, Toplam Skor: {oyuncu_skoru(oyuncu_kartlari)}")
    await ctx.send(f"Krupiye Kartları: {krupiye_kartlari}, Toplam Skor: {oyuncu_skoru(krupiye_kartlari)}")

    await ctx.send(kazanan_kontrolu(oyuncu_skoru(oyuncu_kartlari), oyuncu_skoru(krupiye_kartlari)))


@bot.command()
async def buton(ctx):
    button1 = Button(label="Seçim 1", style=discord.ButtonStyle.primary)
    button2 = Button(label="Seçim 2", style=discord.ButtonStyle.danger)
    view = View()
    view.add_item(button1)
    view.add_item(button2)

    async def button1_callback(interaction):
        await interaction.response.send_message("Seçim 1'i seçtiniz")
    async def button2_callback(interaction):
        await interaction.response.send_message("Seçim 2'yi seçtiniz")

    button1.callback = button1_callback
    button2.callback = button2_callback
    await ctx.send("Deneme", view=view)



    

bot.run("YOUR TOKEN :) ")
