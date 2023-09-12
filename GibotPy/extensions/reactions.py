import lightbulb
import pickle
from os import path, listdir
from GibotPy.utils import config

DATA = path.join(path.dirname(__file__), "../../Data")
print(listdir(DATA))

plugin = lightbulb.Plugin("ReactionPlugin")

    


class ReactionCommandGroup:
    _SAVE_DIR = path.join(DATA, "reaction_commands")

    @staticmethod
    def load_from_id(message_id):
        with open(path.join(ReactionCommandGroup._SAVE_DIR, str(message_id)), "rb") as f:
            return pickle.load(f)

    def __init__(self, message_id):
        self._message_id = message_id
        self._rate_limit_min = 0
        self._commands = {} #key=emoji, value=ReactionCommand object
    
    def set_rate_limit(self, rate_limit_min):
        self.rate_limit = rate_limit_min

    def save(self):
        with open(path.join(ReactionCommandGroup._SAVE_DIR, str(self._message_id)), "wb") as f:
            return pickle.dump(self, f)

class ReactionCommandAlreadyExistsError(Exception):
    pass


class ReactionCommand:
    VALID_SCHEMES = {
        "reaction_role": [
            "add/remove",
            "remove/add",
            "[0-9]+_times"
        ]
    }
    def __init__(
            self, 
            parent: ReactionCommandGroup, 
            execution_scheme, 
            usage_scheme, 
            emoji,
            **kwargs):
        """
        parent is the group that the ReactionCommand belongs to
        execution_scheme: the kind of reaction command that this is
        """
        self.parent = parent
        self.execution_scheme = execution_scheme
        self.usage_scheme = usage_scheme 
        self.emoji = emoji
        if emoji in parent._commands.keys():
            # raising an exception allows us to handle the problem with output
            # to the user. 
            # __init__ cannot be async so we can't do anything more than print
            # if this point of the code is reached
            raise ReactionCommandAlreadyExistsError
        parent._commands[emoji] = self

        if execution_scheme == "reaction_role":
            self.role = kwargs.pop("role")

    def save(self):
        self.parent.save()



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