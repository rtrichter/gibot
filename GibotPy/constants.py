import json
from os import path
import discord

DATA = path.join(path.realpath(__file__), "../../Data")


def get_config(key: str):
    with open(path.join(DATA, "config.json")) as f:
        return json.load(f)[key]


# need to pass bot to avoid some sort of circular import issue
def get_guild(client) -> discord.Guild:
    return client.get_guild(get_config("guild_id"))


def get_role(guild, role_name: str) -> discord.Role:
    return guild.get_role(get_config("role_ids")[role_name])


