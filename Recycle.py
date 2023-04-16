import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}! Я помогу тебе сохранить окружающую среду')

@bot.command()
async def helping(ctx):
    await ctx.send(f'Вот команды которые есть во мне:')
    await ctx.send(f'!hello')
    await ctx.send(f'!rubbish rub (название предмета) - например !rubbish rub  шина')
    await ctx.send(f'!bin')
    await ctx.send(f'!ecology')
    await ctx.send(f'!recommendation')
@bot.command()
async def video(ctx):
    vids = os.listdir('Vid')
    vidd = random.choice(vids)
    with open(f'Vid/{vidd}', 'rb') as f:
        video = discord.File(f)
    await ctx.send(file=video)

@bot.command()
async def rubbish(ctx, rub):  # !rubish пластиковый пакет
    await ctx.send(rubish_choice(rub))

@bot.command()
async def bin(ctx):  # !rubish пластиковый пакет
    with open('Bin1/Bin.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send("Есть 4 видов мусорных баков")
    await ctx.send(file=picture)
    
@bot.command()
async def ecology(ctx):
    await ctx.send(f'Эколо́гия — естественная наука (раздел биологии) о взаимодействиях живых организмов между собой и с их средой обитания, об организации и функционировании биосистем различных уровней (популяции, сообщества, экосистемы).' f' В просторечии под экологией часто понимается состояние окружающей среды, а под экологическими проблемами — вопросы охраны окружающей среды от воздействия антропогенных факторов. Экологизм — общественное движение за усиление мер охраны окружающей среды и за предотвращение разрушения среды обитания.')

@bot.command()
async def recommendation(ctx):
    with open('sovetu.txt', 'r', encoding='utf-8') as f:
        sovetu = f.read()
        await ctx.send(sovetu)
        f.close()
        


def rubish_choice(rub):
    recyclable_waste = ["тетрадь", "бумажный пакет", "блокнот", "коробка", "пластиковая бутылка", "аллюминий", "Флюорографическая пленка", "дерево", "бумага" ]
    waste = ["батарейки", "телевизор", "шина", "пластиковый пакет", "пластик", "стекло", "чек"]
    if rub in recyclable_waste:
        message = "Это можно переработать"
    elif rub in waste:
        message = "Это нельзя переработать"
    else:
        message = "Я не знаю, что с этим можно сделать"
    return message


bot.run("MTA5NDU4ODg3ODYyODg1OTkxNQ.G_nylh.KHpD2NetIQ-c1EZqAeIqA7EGEMOBUCM-h1q7gc")