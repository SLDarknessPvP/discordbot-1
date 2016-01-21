from foxxbot import FoxxBot
import logging


def setup_logging():
    logging.basicConfig(filename="foxxbot.log",level=logging.DEBUG)


if __name__ == "__main__":
      setup_logging()
      b = FoxxBot() 
      b.load_extension("commands")
      b.load_extension("random_commands")
      b.run("user","pass")   
