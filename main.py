import asyncio
import os
from discord.utils import setup_logging
from core import Bot
from dotenv import load_dotenv
 
# Load environment variables from .env file
load_dotenv()

# Get the Discord bot token from environment variables
token = os.environ.get("TOKEN")

async def main() -> None:
    # Set up logging for the bot
    setup_logging()
    async with Bot() as bot:
        # Start the bot and reconnect if disconnected
        await bot.start(token=token, reconnect=True)

if __name__ == "__main__":
    if token is None:
        print("Error: TOKEN environment variable not set.")
    else:
        asyncio.run(main())
