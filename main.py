import discord
import os
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We Have Logged In As {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return


  if 'hello' in message.content.lower():
    await message.channel.send('Hello {}'.format(message.author.name))
  if '!inpire' in message.content.lower():
    await message.channel.send('Hi I Am {0.user}'.format(client))  



keep_alive()
client.run(my_secret)      