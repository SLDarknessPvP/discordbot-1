import discord
import logging
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        command_prefix = "!"
        description = "FoxxBot 2.0, A bot for the unoffical fam"
        super().__init__(command_prefix="!", description=description)
        # self.custom_commands = defaultdict(str)   
    
    async def on_ready(self):
        logging.info("Logged in as")
        logging.info(self.user.name)
        logging.info(self.user.id)
        
    async def on_message(self):
        pass