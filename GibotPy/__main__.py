import bot
from discord.ext import tasks
from os import path
import constants
import rainbow_role 

@bot.client.event
async def on_ready():
    print("Ready")
    bot.guild = bot.client.get_guild(constants.get_config("guild_id"))
    await rainbow_role.rainbow_role_update()

with open(path.join(constants.DATA, "gibot_token.txt"), 'r') as t:
    token = t.read()
bot.client.run(token)