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

# say and ping are just test commands that can be used to make sure the bot is working
# decorator to make a command
@bot.command()
# add a parameter
@lightbulb.option("text", "The thing to say.")
# name of the command (use /say in discord) and the description
@lightbulb.command("say", "Make the bot say something.")
# lets you choose between prefix and slash commands. We will only use slash commands cause prefix commands are less user friendly.  
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_say(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(ctx.options.text)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    """If a non-bot user mentions the bot, respond with 'Pong!'"""

    # do not respond to webhooks nor bots pinging us (only users)
    if not event.is_human:
        return
    me = bot.get_me()
    
    if me.id in event.message.user_mentions_ids:
        await event.message.respond("Pong!")


def run() -> None:
    if name != "nt": # supposedly this is for non-windows things
        import uvloop
        uvloop.install()
    
    bot.run()