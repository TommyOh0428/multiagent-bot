import os
from app import create_app
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)