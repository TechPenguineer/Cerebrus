import discord
import asyncio
import datetime

# LOAD TOKEN FROM JSON
import json
with open('config.json') as f:
    token = json.load(f)['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)