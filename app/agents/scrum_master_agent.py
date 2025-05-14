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

# Determine the directory of the current script (e.g., /.../app/agents)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the instructions file, assuming 'instructions' is a subfolder of 'agents'
# and the instruction file is named 'scrum_master.md'
SCRUM_INSTRUCTION_FILE_PATH = os.path.join(SCRIPT_DIR, "instructions", "scrum_master.md")

class ScrumMasterAgent:
    @staticmethod
    async def get_scrum_response(channel, user_input: str): # Method is now async and parameters updated
        # Get chat history from the specified channel
        chat_history = await get_chat_history(channel)
        
        # Load scrum master instructions
        instructions = load_instructions(SCRUM_INSTRUCTION_FILE_PATH)
        
        # Create a prompt segment with chat history and current user input
        contextual_query = create_prompt(chat_history, user_input)
        
        # Combine instructions and the contextual query for the final prompt
        # The create_prompt function already adds some newlines, so one more should suffice.
        final_api_prompt = f"{instructions}\\n{contextual_query}"
        
        # Call OpenAI API
        scrum_response = openai.completions.create(
            model="gpt-4o",
            prompt=final_api_prompt, # Use the fully constructed prompt
            max_tokens=150 # Retain max_tokens or adjust as needed
            # Removed the 'messages' parameter as it's not for openai.completions.create
        )
        return scrum_response.choices[0].text.strip()