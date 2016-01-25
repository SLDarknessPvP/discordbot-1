import discord
from discord.ext import commands
import logging
from config import Config
import asyncio
import wolframalpha

class FoxxBot(commands.Bot):
    def __init__(self, config):
        description = config.description
        self.config = config
        with open(config.pokemon_file) as f:
            self.pokemon_list = f.read().split("\n")
        self.custom_commands = [] 
        self.wolfram_client = wolframalpha.Client(config.wolfram_id)
        super().__init__(command_prefix="!", description=description)
    
    async def on_ready(self):
        logging.info("Logged in as")
        logging.info(self.user.name)
        logging.info(self.user.id)
    
    async def on_member_join(self, member):
        server = member.server
        fmt = "Welcome {0.mention} to {1.name}"
        await self.say(fmt.format(member, server))    
    
    def activate(self):
        self.run(self.config.email, self.config.password)    
        
config = Config("src/config/bot_settings.json")
bot = FoxxBot(config)
for cog in config.cogs:
    bot.load_extension(cog)
    
@bot.command()
async def add(name : str, *msg : str):
    """Add a custom text response command."""   
    response = " ".join(msg)
    if name not in bot.custom_commands:
        bot.custom_commands.append(name)    
        f = asyncio.coroutine(lambda: bot.say(response))
        cmd = commands.Command(name,callback=f,help=response)
        bot.add_command(cmd)
        await bot.say("{} command added.".format(name))
    else:
        await bot.say("Can't overwrite other commands.")   

@bot.command()
async def remove(name : str):
    """Removes a custom added response command."""
    if name in bot.custom_commands:
        bot.custom_commands.remove(name)
        bot.remove_command(name)        
        await bot.say("{} command removed.".format(name))    
    
def get_bot():
    return bot