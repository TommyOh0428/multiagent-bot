import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
from helper import load_instructions

load_dotenv()

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

class ScrumMasterAgent:
    @staticmethod
    def get_scrum_response(input_text: str):
        scrum_response = openai.completions.create(
            model="gpt-4o",
            prompt=input_text,
            max_tokens=150,
        )
        return scrum_response.choices[0].text.strip()