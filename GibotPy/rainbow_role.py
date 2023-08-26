from discord.ext import tasks, commands
import random
import constants
from os import path
import asyncio
import bot

previous_color = 0

def cog_unload():
    rainbow_role_update.cancel()

# initialize the rainbow role update loop
# @tasks.loop(seconds=constants.rainbow_role_update_period_s) 
async def rainbow_role_update():
    await bot.bot.wait_until_ready()
    print("updating color")
    while True:
        new_color = random.choice(list(constants.get_config("color_hex").values()))
        if new_color != previous_color:
            break
    rainbow_role = constants.get_role(bot.guild, "rainbow")
    await rainbow_role.edit(color=new_color)
    await asyncio.sleep(constants.rainbow_role_update_period_s)
    await rainbow_role_update() # idk what's going on with the loops so after the delay just call the function again

