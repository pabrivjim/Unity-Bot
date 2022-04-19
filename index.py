import discord 
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import random
import asyncio

TOKEN = "TU TOKEN"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "?", intents=intents, case_insensitive= True)
print("running")

async def is_owner(ctx):
    return ctx.author.id == 328123657153150978

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Unity Bot | ?help"))
    print("Bot is ready!")

@bot.command()
@commands.check(is_owner)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.check(is_owner)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


    

        



bot.run(TOKEN)