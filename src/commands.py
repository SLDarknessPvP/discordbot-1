from discord.ext import commands
import aiohttp
import logging



class FoxxBotCog():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def twitch(self,user : str):
        """returns a twitch channel, if a user is live."""
        url = "https://api.twitch.tv/kraken/streams/{}".format(user)
        res = await aiohttp.get(url)
        link = "https://twitch.tv/{}".format(user)
        async with aiohttp.get(url) as res:            
            try:
                content = await res.json()
                is_live = content["stream"]
            except KeyError:
                await self.boy.say("Sorry user could not be found.")
            else:
                if is_live is None:
                    bot_res = "Sorry {} is not live".format(user)
                else:
                    bot_res = "{} is live! Watch Now! {}".format(user,link)
        
        await self.bot.say(bot_res)



def setup(bot):
    bot.add_cog(FoxxBotCog(bot))
