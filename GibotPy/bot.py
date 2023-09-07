import discord
from discord import app_commands
from discord.ext import commands
from os import path

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)
guild = None # this is updated on ready