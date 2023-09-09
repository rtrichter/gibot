from os import path, name
import hikari
import lightbulb
from lightbulb.ext import tasks

from GibotPy.utils import config

with open(path.join(config.DATA, "gibot_token.txt")) as f:
    TOKEN = f.read()

bot = lightbulb.BotApp(
    TOKEN,
    default_enabled_guilds=config.get_config("guild_id"),
    help_slash_command=True,
    intents=hikari.Intents.ALL,
)
tasks.load(bot)


bot.command()
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("say", "Make the bot say something.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(ctx.options.text)



def run() -> None:
    if name != "nt":
        import uvloop
        uvloop.install()
    
    bot.run()