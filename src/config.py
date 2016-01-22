import json


class Config(object):
    def __init__(self,filename):
        with open(filename) as f:
            config = json.load(f)
        
        self.name = config["name"]
        self.version = config["version"]
        self.cogs = config["cogs"]
        self.username = config["username"]
        self.password = config["password"]