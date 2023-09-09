import lightbulb
import random
from lightbulb.ext import tasks
import os
from GibotPy.utils import config
from GibotPy.bot import bot

plugin = lightbulb.Plugin("RainbowRolePlugin")


last_color = 0
@tasks.task(s=5)
async def change_rainbow_color():
    """"""
    print("updating color")
    # this will make change_rainbow_color.last_color act like a static variable
    # if not hasattr(change_rainbow_color, "last_color"):
    #     change_rainbow_color.last_color = 0
    # colors is a dict. (key=color name, value=hex code)
    colors = config.get_config("colors")
    # the loop lets us make sure we don't repeat a color twice in a row
    timeout = 0
    max_timeout = 10000
    new_color = last_color
    while new_color == last_color:
        # if something ever goes wrong we shouldn't get stuck here
        if timeout > max_timeout:
            return
        # select a random 
        new_color = random.choice(list(colors.keys()))
    # update the color
    print(new_color)
    await bot.rest.edit_role(config.get_config("guild_id"), config.get_config("role_ids")["rainbow"], color=colors[new_color])
    

def initialize():
    """
    This is used to initialize any commands, tasks, etc. in this file
    """
    print("Initializing rainbow role")
    change_rainbow_color.start()

