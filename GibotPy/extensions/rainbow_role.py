import lightbulb
import random
from lightbulb.ext import tasks
import os
from GibotPy.utils import config
# from GibotPy.bot import bot

plugin = lightbulb.Plugin("RainbowPlugin")

last_color = 0
@tasks.task(s=config.get_config("rainbow_role_update_period_s"))
async def change_rainbow_color():
    """
    This task runs at time intervals defined by config->rainbow_role_update_period_s. 
    It will set the color of rainbow role to a random color every time it runs 
    
    """
    # colors is a dict. (key=color name, value=hex code)
    colors = config.get_config("colors")
    # the loop lets us make sure we don't repeat a color twice in a row
    timeout, max_timeout = 0, 10000
    new_color = last_color
    while new_color == last_color:
        # if something ever goes wrong we shouldn't get stuck here
        if timeout > max_timeout:
            return
        # select a random 
        new_color = random.choice(list(colors.keys()))
    # update the color
    await plugin.bot.rest.edit_role(config.get_config("guild_id"), config.get_config("role_ids")["rainbow"], color=colors[new_color])
    
    

def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)
    change_rainbow_color.start()

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)

