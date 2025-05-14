import os
import discord
from discord.ext import commands
from .agents.scrum_master_agent import ScrumMasterAgent
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("/scrum"):
        response = await ScrumMasterAgent.get_scrum_response(message.channel, message.content)
        await message.channel.send(response)