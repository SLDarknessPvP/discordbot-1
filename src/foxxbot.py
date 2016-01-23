import discord
from discord.ext import commands
import logging
from config import Config
import asyncio

class FoxxBot(commands.Bot):
    def __init__(self, config):
        description = "FoxxBot 2.0! A bot for the unofficial fam!"
        self.config = config
        super().__init__(command_prefix="!", description=description)
    
    async def on_ready(self):
        logging.info("Logged in as")
        logging.info(self.user.name)
        logging.info(self.user.id)
    
    async def on_member_join(self, member):
        server = member.server
        fmt = "Welcome {0.mention} to {1.name}"
        await self.say(fmt.format(member,server))    
    
    def activate(self):
        self.run(self.config.username, self.config.password)    
        
config = Config("src/config/bot_settings.json")
bot = FoxxBot(config)
for cog in config.cogs:
    bot.load_extension(cog)
    
@bot.command()
async def add(name : str, *msg : str):
    """Add a custom text response to the bot"""   
    f = asyncio.coroutine(lambda: bot.say(" ".join(msg)))
    cmd = commands.Command(name,callback=f)
    bot.add_command(cmd)
    await bot.say("command added")

@bot.command()
async def remove(name : str):
    bot.remove_command(name)        
    await bot.say("command removed")    
        
def get_bot():
    return bot        