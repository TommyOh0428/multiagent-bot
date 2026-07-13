def load_instructions(file_path: str) -> str:
    """Load an agent instruction file."""
    with open(file_path, "r") as file:
        return file.read()


async def get_chat_history(channel, limit: int = 10) -> str:
    """Return recent Discord channel messages in chronological order."""
    chat_history = []
    async for message in channel.history(limit=limit):
        chat_history.append(f"{message.author.name}: {message.content}")

    chat_history.reverse()
    return "\n".join(chat_history)


def create_prompt(chat_history: str, user_input: str) -> str:
    """Combine conversation history with the current user input."""
    return f"""
            Chat History:
            {chat_history}

            User Input:
            {user_input}
            """
