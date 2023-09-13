import lightbulb
import hikari
# from hikari.impl.cache import CacheImpl as cache 
import pickle
from os import path, listdir, remove
from GibotPy.utils import config

DATA = path.join(path.dirname(__file__), "../../Data")
print(listdir(DATA))

plugin = lightbulb.Plugin("ReactionPlugin")

    

REACTION_SAVE_DIR = path.join(DATA, "reaction_commands")

class ReactionRole:
    @staticmethod
    def group_exists(channel_id, message_id):
        return f"{channel_id}.{message_id}" in listdir(REACTION_SAVE_DIR)

    @staticmethod
    def command_exists(channel_id, message_id, emoji):
        # if there is no file for this message
        if not ReactionRole.group_exists(channel_id, message_id):
            return
        # if there is a file, load the object
        group = ReactionRole.load(channel_id, message_id)
        # and check for that command
        return emoji in group._commands.keys()

    @property
    def path(self):
        return path.join(REACTION_SAVE_DIR, f"{str(self._channel_id)}.{str(self._message_id)}")

    def save(self):
        with open(self.path, "wb") as f:
            return pickle.dump(self, f)
    
    @staticmethod
    def load(channel_id, message_id):
        with open(path.join(REACTION_SAVE_DIR, f"{str(channel_id)}.{str(message_id)}"), "rb") as f:
            return pickle.load(f)

    @staticmethod
    def reset(channel_id, message_id):
        remove(path.join(REACTION_SAVE_DIR, f"{str(channel_id)}.{str(message_id)}"))

    def __init__(self, channel_id, message_id, usage_scheme):
        # if the message is already initialized load it
        if str(message_id) in listdir(REACTION_SAVE_DIR):
            self = ReactionRole.load(message_id)
            return
        # otherwise initialize it
        self._channel_id = channel_id
        self._message_id = message_id
        self._usage_scheme = usage_scheme
        self._commands = {}
        self.save()

    def add(self, emoji, role):
        self._commands[emoji] = role
        self.save()

    def remove(self, emoji):
        self._commands.pop(emoji)
        self.save()

    def __str__(self):
        channel_id = f"channel_id={self._channel_id} \n"
        message_id = f"message_id={self._message_id} \n"
        usage_scheme = f"usage_scheme={self._usage_scheme} \n"
        commands = "commands: \n"
        for key in self._commands:
            commands += f"    {key} : {self._commands[key]} \n"
        return channel_id + message_id + usage_scheme + commands
    
    def get_role_id(self, emoji):
        return int(self._commands[emoji][3:-1])


@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(config.get_config("role_ids")["Admin"]))
@lightbulb.option("channel_id", "id of the message that will hold the reaction command")
@lightbulb.option("message_id", "id of the message that will hold the reaction command")
@lightbulb.option("usage_scheme", "A variant of an execution scheme")
@lightbulb.command("rr_init", "Creates a new reaction command")
@lightbulb.implements(lightbulb.SlashCommand)
async def rr_init(ctx: lightbulb.SlashContext):
    print(f"Creating new reaction_role command...")
    ReactionRole(ctx.options.channel_id, ctx.options.message_id, ctx.options.usage_scheme)
    await ctx.respond("Reaction Role initialized")

@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(config.get_config("role_ids")["Admin"]))
@lightbulb.option("channel_id", "id of the channel that will hold the reaction command")
@lightbulb.option("message_id", "id of the message that will hold the reaction command")
@lightbulb.option("emoji", "The emoji that will be associated with this role")
@lightbulb.option("role", "The role to give/take when a member reacts")
@lightbulb.command("rr_add", "adds a reaction function to the reaction command")
@lightbulb.implements(lightbulb.SlashCommand)
async def rr_add(ctx: lightbulb.SlashContext):
    print(f"Adding command ({ctx.options.emoji}) to reaction command group ({ctx.options.message_id})")
    # load the command group
    group = ReactionRole.load(ctx.options.channel_id, ctx.options.message_id)
    group.add(ctx.options.emoji, ctx.options.role)
    await plugin.bot.rest.add_reaction(group._channel_id, group._message_id, ctx.options.emoji)
    await ctx.respond("Reaction Role added")

@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(config.get_config("role_ids")["Admin"]))
@lightbulb.option("channel_id", "id of the channel that will hold the reaction command")
@lightbulb.option("message_id", "id of the message that will hold the reaction command")
@lightbulb.option("emoji", "The emoji that will be associated with this role")
@lightbulb.command("rr_rm", "removes a reaction function from the reaction command")
@lightbulb.implements(lightbulb.SlashCommand)
async def rr_rm(ctx: lightbulb.SlashContext):
    print(f"Removing command ({ctx.options.emoji}) from reaction command group ({ctx.options.message_id})")
    # load the command group
    group = ReactionRole.load(ctx.options.channel_id, ctx.options.message_id)
    group.remove(ctx.options.emoji)
    await ctx.respond("Reaction Role removed")

@plugin.command
@lightbulb.add_checks(lightbulb.has_roles(config.get_config("role_ids")["Admin"]))
@lightbulb.option("channel_id", "id of the channel that will hold the reaction command")
@lightbulb.option("message_id", "id of the message that will hold the reaction command")
@lightbulb.command("rr_info", "removes a reaction function from the reaction command")
@lightbulb.implements(lightbulb.SlashCommand)
async def rr_info(ctx: lightbulb.SlashContext):
    group = ReactionRole.load(ctx.options.channel_id, ctx.options.message_id)
    print(group)
    await ctx.respond(str(group))

@plugin.listener(hikari.events.ReactionAddEvent)
async def detect_reaction_add(event: hikari.events.ReactionAddEvent):
    if not ReactionRole.command_exists(event.channel_id, event.message_id, event.emoji_name):
        return
    group = ReactionRole.load(event.channel_id, event.message_id)
    await plugin.bot.rest.add_role_to_member(config.get_config("guild_id"), event.user_id, group.get_role_id(event.emoji_name))

@plugin.listener(hikari.events.ReactionDeleteEvent)
async def detect_reaction_rm(event: hikari.events.ReactionAddEvent):
    if not ReactionRole.command_exists(event.channel_id, event.message_id, event.emoji_name):
        return
    group = ReactionRole.load(event.channel_id, event.message_id)
    await plugin.bot.rest.remove_role_from_member(config.get_config("guild_id"), event.user_id, group.get_role_id(event.emoji_name))


def load(bot: lightbulb.BotApp):
    bot.add_plugin(plugin)

def unload(bot: lightbulb.BotApp):
    bot.remove_plugin(plugin)