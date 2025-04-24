# function to open instructions file
def load_instructions(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

# function to get chat history
async def get_chat_history(channel, limit=10):
    chat_history = []
    async for msg in channel.history(limit=limit):
        chat_history.append(f"{msg.author.name}: {msg.content}")

    chat_history.reverse()
    return "\n".join(chat_history)

# function to create prompt with chat history and user input
def create_prompt(chat_history: str, user_input: str) -> str:
    return f"""
            Chat History:
            {chat_history}

            User Input:
            {user_input}
            """