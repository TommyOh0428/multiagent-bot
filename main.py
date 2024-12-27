import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

# Create a bot instance
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

def main():
    bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    main()