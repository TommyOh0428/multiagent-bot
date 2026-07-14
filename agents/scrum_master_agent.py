import os

import openai
from dotenv import load_dotenv

from agents.helper import create_prompt, get_chat_history, load_instructions


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRUM_INSTRUCTION_FILE_PATH = os.path.join(
    SCRIPT_DIR, "instructions", "scrum-master.md"
)


class ScrumMasterAgent:
    @staticmethod
    def _get_openai_response(user_input: str, chat_history_str: str = ""):
        """Synchronously get a response from OpenAI."""
        instructions = load_instructions(SCRUM_INSTRUCTION_FILE_PATH)
        contextual_query = create_prompt(chat_history_str, user_input)

        scrum_response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": contextual_query},
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return scrum_response.choices[0].message.content.strip()

    @staticmethod
    async def get_scrum_response(channel, user_input: str):
        """Get a response, including Discord chat history when available."""
        chat_history = await get_chat_history(channel) if channel else ""
        return ScrumMasterAgent._get_openai_response(user_input, chat_history)

    @staticmethod
    def get_scrum_response_for_interaction(user_input: str):
        """Get a response for a stateless Discord interaction."""
        return ScrumMasterAgent._get_openai_response(user_input)
