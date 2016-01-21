from bot import Bot
import logging


def setup():
    logging.basicConfig(filename="foxxbot.log",level=logging.DEBUG)


if __name__ == "__main__":
      setup()
      b = Bot() 
      b.run("user","pass")   
