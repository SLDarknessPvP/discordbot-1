import json


class Config(object):
    def __init__(self,filename):
        with open(filename) as f:
            config = json.load(f)
        
        self.username = config["username"]
        self.version = config["version"]
        self.cogs = config["cogs"]
        self.email = config["email"]
        self.password = config["password"]
        self.pokemon_file = config["pokemon"]
        self.description = config["description"]
        self.wolfram_id = config["wolfram_id"]