import discord
from discord.ext import commands
import logging
from config import Config
import asyncio
import aiohttp
import json
import wolframalpha

class FoxxBot(commands.Bot):
    def __init__(self, config):
        description = config.description
        self.config = config
        with open(config.pokemon_file) as f:
            self.pokemon_list = f.read().split("\n")
        self.custom_commands = [] 
        self.wolfram_client = wolframalpha.Client(config.wolfram_id)
        with open("src/config/emote2id.json") as f:
            self.emote_map = json.load(f)
        
        super().__init__(command_prefix="!", description=description)
    
    async def on_ready(self):
        logging.info("Logged in as")
        logging.info(self.user.name)
        logging.info(self.user.id)
    
    async def on_member_join(self, member):
        server = member.server
        fmt = "Welcome {0.mention} to {1.name}"
        await self.say(fmt.format(member, server))    
    
    async def on_message(self, message):
        if message.author == self.user:
            return
   
        splt = message.content.split()
        intersection = set(splt) & set(self.emote_map.keys())
        if intersection:
            for emote_name in intersection:
                fname = "src/emotes/{}.png".format(emote_name)    
                try:
                    with open(fname,"rb") as fp:
                        await self.send_file(message.channel, fp)
                except FileNotFoundError:
                    emote_id = self.emote_map[emote_name]
                    url = "http://static-cdn.jtvnw.net/emoticons/v1/{}/1.0".format(emote_id)
                    print (url)
                    async with aiohttp.get(url) as res:
                        content = await res.read()
                        with open(fname,"wb") as fp:
                            fp.write(content)
                        with open(fname,"rb") as fp:
                            await self.send_file(message.channel, fp)           
        await self.process_commands(message)    
    
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