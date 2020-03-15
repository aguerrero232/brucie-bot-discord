import os

import random
import discord
from dotenv import load_dotenv

load_dotenv()

brucie_quotes = [
    'time to play hooman!',
    'WOOF!!',
    'BARK BARK BARK BARK BARK'
]

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}( id: {guild.id})'
    )

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
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
