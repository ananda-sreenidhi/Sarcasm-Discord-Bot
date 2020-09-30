import discord
from discord.ext import commands
import os

token = open("token.txt", "r").read()
client = commands.Bot(command_prefix = "!")

initial_extensions = ['cogs.sarc']

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for extension in initial_extensions:
    client.load_extension(extension)
client.run(token)
