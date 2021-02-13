import discord, matplotlib.pyplot as plt, numpy as np
from math import *

client = discord.Client()

# testing server id: 810149199488352256

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  id = client.get_guild(810149199488352256)
  
  if message.author == client.user:
    return

  if message.content.startswith('~hi'):
    await message.channel.send("hey")
  
  # MAKING AN ANNOUNCEMENT
  if message.content.startswith('~announcement'):
    await message.channel.purge(limit=1)
    await message.channel.send(f"@everyone\n```diff\n+Announcement\n{message.content[13:]}```")

client.run('Token Goes Here')