import discord
from discord.ext import commands
import logging

class FoxxBot(commands.Bot):
    def __init__(self):
        description = "Foxx Bot 2.0! A bot for the unofficial fan"
        super().__init__(command_prefix="!", description=description)
    
    async def on_ready(self):
        logging.info("Logged in as")
        logging.info(self.user.name)
        logging.info(self.user.id)