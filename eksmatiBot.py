import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event #create a new event handler
async def on_message(message): #shows what to do when someone sends a message
    if message.author == client.user: #To make sure the bot won't respond to itself
        return

    if message.content == "Set me a reminder":
        await message.channel.send("Please tell me the name of your event")
        message.content == ""
        await client.wait_for("message")
        reminder = message.content
        await message.channel.send("Reminder set for " + reminder)


client.run(str(TOKEN))
