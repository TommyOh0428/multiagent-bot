import os
import openai
from dotenv import load_dotenv
from app.helper import load_instructions, get_chat_history, create_prompt

load_dotenv()

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Determine the directory of the current script 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRUM_INSTRUCTION_FILE_PATH = os.path.join(SCRIPT_DIR, "instructions", "scrum_master.md")

class ScrumMasterAgent:
    @staticmethod
    def _get_openai_response(user_input: str, chat_history_str: str = ""):
        """Synchronous core logic to get response from OpenAI."""
        instructions = load_instructions(SCRUM_INSTRUCTION_FILE_PATH)
        contextual_query = create_prompt(chat_history_str, user_input)
        final_api_prompt = f"{instructions}\\n{contextual_query}"
        
        scrum_response = openai.completions.create(
            model="gpt-4o",
            prompt=final_api_prompt,
            max_tokens=150,
            temperature=0.7 
        )
        return scrum_response.choices[0].text.strip()

    @staticmethod
    async def get_scrum_response(channel, user_input: str): # For discord.py bot with channel context
        """Asynchronously gets scrum response, including chat history if channel is provided."""
        chat_history = ""
        if channel: # Safely get chat history if channel object is available
            chat_history = await get_chat_history(channel)
        
        return ScrumMasterAgent._get_openai_response(user_input, chat_history_str=chat_history)

    @staticmethod
    def get_scrum_response_for_interaction(user_input: str): # New synchronous method for interactions
        """Gets scrum response based on user input, without prior chat history.
           Suitable for slash commands handled via webhooks.
        """
        return ScrumMasterAgent._get_openai_response(user_input, chat_history_str="")