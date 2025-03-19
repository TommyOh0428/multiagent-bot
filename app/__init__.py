import os
import discord
from discord.ext import commands
from agents.scrum_master_agent import ScrumMasterAgent
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("/scrum"):
        chat_history = []
        async for msg in message.channel.history(limit=10):
            chat_history.append(f"{msg.author.name}: {msg.content}")

        chat_history.reverse()
        input_text = "\n".join(chat_history)
        response = ScrumMasterAgent.get_scrum_response(input_text)
        await message.channel.send(response)