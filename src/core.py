#
# ----- notes
# ----------------------------------------------------------------------------------------

# ----- libraries
# ----------------------------------------------------------------------------------------
from src.config import secret
import discord
import json
from discord.ext import commands


# ----- abstract
# ----------------------------------------------------------------------------------------
class Config:
    def __init__(self, data):
        self.__dict__ = data


# ----- variables
# ----------------------------------------------------------------------------------------
with open("src/config/config.json", "r") as file:
    configdata = json.load(file)

config = Config(configdata);

# ----- functions
# ----------------------------------------------------------------------------------------
def start():

    # definitions
    myIntents = discord.Intents.default();

    client = commands.Bot(command_prefix=config.prefix, intents=myIntents);

    # event handlers
    @client.event
    async def on_ready():
        ready_msg = f"☑️  {client.user} is online!"; 
        print(ready_msg);

    # login
    client.run(secret.token);

# ----- main 
# ----------------------------------------------------------------------------------------
def main():
    start()