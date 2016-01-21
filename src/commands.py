from bot import Bot

b = Bot()

@b.event
async def on_ready():
    print ("Logged in as")
    print (b.user.name)
    print (b.user.id)
    print ("------")

@b.command()
async def roll(dice : str):
    """Rolls a dice in NdN format"""
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await b.say("Format has to be in NdN!")
        return
    result = ",".join(str(random.randint(1,limit)) for r in range(rolls))
    await b.say(result)
