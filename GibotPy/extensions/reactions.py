import lightbulb
import json
from os import path, listdir
from GibotPy.utils import config

DATA = path.join(path.dirname(__file__), "../../Data")
print(listdir(DATA))

plugin = lightbulb.Plugin("ReactionPlugin")

    


class ReactionCommandGroup:
    def __init__(self, message_id):
        self.message_id = message_id
        self.commands = {} #key=emoji, value=ReactionCommand object

    def save(self):
        with open():
            pass

class ReactionCommandAlreadyExistsError(Exception):
    pass


class ReactionCommand:
    def __init__(self, parent: ReactionCommandGroup, execution_scheme, usage_scheme, emoji):
        """
        parent is the group that the ReactionCommand belongs to
        execution_scheme: the kind of reaction command that this is
        """
        self.parent = parent
        self.execution_scheme = execution_scheme
        self.usage_scheme = usage_scheme 
        self.emoji = emoji
        if parent.commands.has_key(emoji):
            raise ReactionCommandAlreadyExistsError
            # not sure if this is reachable but if it is, 
            # it stops us from overwriting anything
            return 
        parent.commands[emoji] = self



@plugin.command
@lightbulb.implements(lightbulb.SlashCommand)
@lightbulb.add_checks(lightbulb.has_roles(config.get_config("role_ids")["Admin"]))
@lightbulb.option("message_id", "id of the message that will hold the reaction command")
@lightbulb.option("emoji", "The emoji to be associated with the reaction command")
@lightbulb.command("new_command", "Creates a new reaction command")
async def new_reaction_role(ctx: lightbulb.SlashContext):
    print("Creating new reaction_role command...")



def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)