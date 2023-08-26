import discord
from discord import app_commands
from os import path
import constants

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guild = None # this is updated on ready