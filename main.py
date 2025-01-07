import os
from bot import bot
from app import create_app
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

if __name__ == '__main__':
    app = create_app()
    bot.run(DISCORD_TOKEN)
    app.run(port=5000)