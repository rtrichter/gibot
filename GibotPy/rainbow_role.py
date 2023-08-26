import bot
from discord.ext import tasks
import random
import constants
from os import path

previous_color = 0

# initialize the rainbow role update loop
@tasks.loop(seconds=constants.rainbow_role_update_period_s) 
async def rainbow_role_update():
    await bot.client.wait_until_ready()
    while True:
        new_color = random.choice(list(constants.get_config("color_hex").values()))
        if new_color != previous_color:
            break
    rainbow_role = constants.get_role(bot.guild, "rainbow")
    print(new_color)
    await rainbow_role.edit(color=new_color)

