from bot import get_bot
import logging


def setup_logging():
    logging.basicConfig(filename="foxxbot.log",level=logging.ERROR)


setup_logging()
b = get_bot()      
b.activate()     