
import os

import discord

from slotmachine import SlotMachine

# Sample simulations
slot1 = SlotMachine(3, {"777": 300, "888": 300, "999": 300})
slot2 = SlotMachine(4, {
  '7': 1,
  '77': 10,
  '777': 150,
  '7777': 1000
  })

print(slot1.simulation(100000, 20000, 2))
print(slot2.simulation(1000000, 20000, 2))


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e