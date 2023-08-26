import bot
from discord.ext import tasks
from os import path
import constants
import rainbow_role 


@bot.bot.event
async def on_ready():
    print("Ready")
    # update guild
    bot.guild = bot.bot.get_guild(constants.get_config("guild_id"))

    # start loops
    await rainbow_role.rainbow_role_update() # starts the rainbow update loop


with open(path.join(constants.DATA, "gibot_token.txt"), 'r') as t:
    token = t.read()
bot.bot.run(token)