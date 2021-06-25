#!/usr/bin/env python3

import os
import random
from os.path import join

import discord

from discord.ext import commands
from dotenv import load_dotenv

from env import DISCORD_TOKEN
from env import DISCORD_GUILD

load_dotenv()
client = discord.Client()

bot = commands.Bot(command_prefix='$')

TOKEN = DISCORD_TOKEN
GUILD = DISCORD_GUILD

brucie_quotes = ['time to play hooman!', 'WOOF!!', 'BARK BARK BARK BARK BARK']

memeCmds = {"lovelife", "deny", "anime", "facts", "nsfw", "pokemon", "life", "meme", "wtf", "agree", "computerscience",
            "spongebob", "covid19", "hoefosho",
            "ww3", "school", "politics", "swear", "religious", "compliment", "smile", "animals", "beard", "gaming",
            "dissagree", "tigerking", "insult", "defense"}


@bot.command()
async def lovelife(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/lovelife'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def deny(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/deny'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def anime(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/anime'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def facts(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/facts'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def nsfw(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/nsfw'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def pokemon(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/pokemon'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def life(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/life'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def meme(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/meme'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def wtf(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/wtf'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def agree(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/agree'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def computerscience(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/computerscience'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def spongebob(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/spongebob'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def covid19(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/covid19'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def ww3(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/ww3'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def school(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/school'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def politics(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/politics'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def swear(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/swear'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def compliment(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/compliment'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def smile(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/smile'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def animals(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/animals'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def beard(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/beard'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def gaming(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/gaming'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def dissagree(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/dissagree'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def tigerking(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/tigerking'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def insult(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/insult'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def defense(ctx):
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/defense'
    filename = random.choice([x for x in os.listdir(dir)])
    await ctx.send(file=discord.File(dir + '/' + filename))


@bot.command()
async def test(ctx):
    await ctx.send('I am working!')


@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')
    print('Bot is ready.')
    print('----------')

    await bot.change_presence(status=discord.Status.online, activity=discord.Game('fetch'))


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' Welcome {member.name}, to the {GUILD} server!'
    )

bot.run(TOKEN)
