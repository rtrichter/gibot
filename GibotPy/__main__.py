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

    # add cogs
    await bot.bot.add_cog(rainbow_role.Rainbow(bot.bot, bot.guild))

    # start loops
    # await rainbow_role.rainbow_role_update_loop() # starts the rainbow update loop
    



with open(path.join(constants.DATA, "gibot_token.txt"), 'r') as t:
    token = t.read()
bot.bot.run(token)