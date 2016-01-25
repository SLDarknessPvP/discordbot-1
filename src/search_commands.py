from discord.ext import commands
from giphypop import Giphy
import wikipedia
import wolframalpha
import asyncio

class SearchCommands():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def giphy(self, *q : str):
        """Returns a random gif from a giphy search of phrase"""
        g = Giphy()
        phrase = " ".join(q)
        results = [x for x in g.search(phrase)]
        img = random.choice(results)
        await self.bot.say(img.media_url)
    
    
    @commands.command()
    async def wolframalpha(self, *, q : str):
        """Searchs wolframalpha for the given term"""
        result = self.bot.wolfram_client.query(q)     
        #not all wolfram queries have results section
        #default to the first pod 
        try:
            bot_msg = next(result.results).text
        except (AttributeError, StopIteration):
            bot_msg = result.pods[1].text
        
        await self.bot.say(bot_msg)     
    
    @commands.command(description="You can then run !wiki on a given item returned")
    async def wikisearch(self, *, q : str):
        """Returns a list of wikipedia articles related search term""" 
        search_results = wikipedia.search(q)
        #limit bot results to 5 to avoid long messages
        msg = "\n".join(search_results[:5])  
        await self.bot.say(msg)
    
    @commands.command()
    async def wiki(self, *, q : str):
        """Returns a 1 sentence summary and link to wiki article"""
        try: 
            page = wikipedia.page(q)
        except wikipedia.exceptions.DisambiguationError:
            await self.bot.say("Could not find Page :(")
        else:
            summary = wikipedia.summary(q,sentences=1)
            msg = "{}\n{}".format(page.url,summary)
            await self.bot.say(msg)
            
def setup(bot):
    bot.add_cog(SearchCommands(bot))