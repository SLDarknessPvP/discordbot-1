import discord
from discord.ext import commands
import random

description = "Testing new discord.ext.commands"
bot = commands.Bot(command_prefix="!", description=description)


@bot.event
async def on_ready():
    print ("Logged in as ")
    print (bot.user.name)
    print (bot.user.id)
    print ("-------")

@bot.command()
async def add(left : int, right : int):
    """adds two numbers together"""
    await bot.say(left+right)

@bot.command(description="For when you wanna settle the score some other way")
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

bot.run("username","pass")
    
   