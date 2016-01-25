from discord.ext import commands
import random
import logging

class RandomCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, *choices : str):
        """Picks a random choice from choices."""
        await self.bot.say(random.choice(choices))
    
    @commands.command()
    async def flip(self):
        """Flips a coin."""
        result = "HEADS!" if random.randint(1,2) % 2 else "TAILS"
        await self.bot.say(result)
    
    @commands.command()
    async def roll(self, dice : str):
        """Rolls a dice in NdN format."""
        try:   
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await self.bot.say("Format has to be in NdN!")
            return 
        
        result = ",".join(str(random.randint(1,limit)) for r in range(rolls))
        await self.bot.say(result)    
       
    @commands.command()
    async def pokemon(self):
        """Displays a random pokemon name"""     
        choice = random.choice(self.bot.pokemon_list)
        await self.bot.say(choice) 

def setup(bot):
    bot.add_cog(RandomCommands(bot))