#!/usr/bin/env python3

import os
import random
from os.path import join

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

#
# for dirs in os.listdir("memes"):
#     print(dirs)
#

brucie_quotes = [
    'time to play hooman!',
    'WOOF!!',
    'BARK BARK BARK BARK BARK'
]

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='$')


memecommandlist={"lovelife","deny","anime","facts","nsfw","pokemon","life","meme","wtf","agree","computerscience","spongebob","covid19","hoefosho",
             "ww3","school","politics","swear","religious","compliment","smile","animals","beard","gaming","dissagree","tigerking","insult","defense"}


client = discord.Client()



@bot.commands
async def lovelife():
    dir = '/home/ariel/PycharmProjects/brucieBot/memes/lovelife'
    filename = random.choice([x for x in os.listdir(dir)])
    await client.channel.send(file=discord.File(dir + '/' + filename))
# async def deny():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def anime():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def facts():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def nsfw():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def pokemon():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def life():
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def meme():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def wtf():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def agree():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def computerscience():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def spongebob():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def covid19():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def hoefosho():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def ww3():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def school():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def politics():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def swear():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def religious():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def compliment():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def smile():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def animals():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def beard():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def gaming():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def dissagree():
#
#
# # dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# # filename=random.choice([x for x in os.listdir(dir)])
# # await message.channel.send(file=discord.File(dir+'/'+filename))
# async def tigerking():


# dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
# filename=random.choice([x for x in os.listdir(dir)])
# await message.channel.send(file=discord.File(dir+'/'+filename))
async def insult():
    dir='/home/ariel/PycharmProjects/brucieBot/memes/insult'
    filename=random.choice([x for x in os.listdir(dir)])
    await commands.channel.send(file=discord.File(dir+'/'+filename))
async def defense():
    dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
    filename=random.choice([x for x in os.listdir(dir)])
    await commands.channel.send(file=discord.File(dir+'/'+filename))


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}( id: {guild.id})'
    )
    await client.change_presence(status=discord.Status.online, activity=discord.Game('fetch'))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f' Welcome {member.name}, to the {GUILD} server!'
    )

@client.event
async def on_message(message):
    if 'happy birthday' in message.content:
        await message.channel.send('Happy Birthday!🎈🎉')
    elif 'toy' in message.content:
        quote = random.choice(brucie_quotes)
        await message.channel.send(quote)
    elif 'get them brucie' in message.content:
        await message.channel.send("GRRRRRRRRRRRRRRRRRRRRRRRRRR")
    elif 'get em brucie' in message.content:
        await message.channel.send("Deez nuts! .... ha WOOF! ")
    # elif '$lovelife' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/lovelife'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$defense' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/defense'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$insult' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/insult'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$tigerking' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/tigerking'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$dissagree' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/dissagree'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$gaming' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/gaming'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$beard' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/beard'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$animals' in message.content:
    #     dir='/home/ariel/PycharmProjects/brucieBot/memes/animals'
    #     filename=random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir+'/'+filename))
    # elif '$smile' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/smile'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$compliment' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/compliment'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$life' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/life'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$religious' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/religious'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$swear' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/swear'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$politics' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/politics'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$school' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/school'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$ww3' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/ww3'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$hoefosho' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/hoefosho'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$covid19' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/covid19'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$spongebob' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/spongebob'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$computerscience' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/computerscience'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$agree' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/agree'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$wtf' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/wtf'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$meme' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/meme'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$pokemon' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/pokemon'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$nsfw' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/nsfw'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$facts' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/facts'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$anime' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/anime'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    # elif '$deny' in message.content:
    #     dir = '/home/ariel/PycharmProjects/brucieBot/memes/deny'
    #     filename = random.choice([x for x in os.listdir(dir)])
    #     await message.channel.send(file=discord.File(dir + '/' + filename))
    elif message.content == 'raise-exception':
        raise discord.DiscordException






client.run(TOKEN)