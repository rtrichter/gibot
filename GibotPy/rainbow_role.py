from discord.ext import tasks, commands
import random
import constants
from os import path
import asyncio
import bot

previous_color = 0


# initialize the rainbow role update loop
# @tasks.loop(seconds=constants.rainbow_role_update_period_s) 
async def rainbow_role_update():
    """Assigns a random color to the rainbow color role every hour"""
    # wait until the bot is ready
    await bot.bot.wait_until_ready()
    # make sure that the color is different than the last color
    while True:
        # get a new color
        new_color = random.choice(
            list(constants.get_config("color_hex").values()))
        # check that it is different from last color
        if new_color != previous_color:
            break
    # get the rainbow discord.Role object
    rainbow_role = constants.get_role(bot.guild, "rainbow")
    # set the color of the rainbow role
    await rainbow_role.edit(color=new_color)
    # delay until the next loop
    await asyncio.sleep(constants.get_config("rainbow_role_update_period_s"))
    # idk what's going on with the loops so after the 
    # delay just call the function again
    await rainbow_role_update() 
