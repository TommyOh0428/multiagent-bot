import os
import discord
from discord.ext import commands
import openai
from dotenv import load_dotenv
from app.helper import load_instructions, get_chat_history, create_prompt

load_dotenv()

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

SCRUM_INSTRUCTION_FILE_PATH = "/instructions/scrum_master.md"

class ScrumMasterAgent:
    @staticmethod
    def get_scrum_response(input_text: str):
        scrum_response = openai.completions.create(
            model="gpt-4o",
            prompt=input_text,
            messages={
                "role": "scrum master",
                "content": load_instructions(SCRUM_INSTRUCTION_FILE_PATH)
            },
            max_tokens=150,
        )
        return scrum_response.choices[0].text.strip()