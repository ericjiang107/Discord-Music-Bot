import discord
from discord.ext import commands
import music
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
ID = os.getenv("CLIENT_ID")

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

cogs = [music]
for i in range(len(cogs)):
    cogs[i].setup(client)


client.run(ID)

