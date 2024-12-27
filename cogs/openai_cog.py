import os
import openai
import discord
from discord.ext import commands
from collections import defaultdict

def load_file(filename: str) -> str:
    """Helper function to read the instructions from a file."""
    instructions_path = os.path.join(os.path.dirname(__file__), "..", "instructions", filename)
    with open(instructions_path, "r", encoding="utf-8") as f:
        return f.read()

class OpenAICog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

        self.system_instructions = {
            "frontend": load_file("frontend.txt"),
            "backend": load_file("backend.txt"),
            "devops": load_file("devops.txt"),
            "scrum-master": load_file("scrum-master.txt")
        }
        self.conversion = defaultdict(list)
        self.channel_id = os.getenv("CHANNEL_1_ID")