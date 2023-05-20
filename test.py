import os
from dotenv import load_dotenv
import telegram
import asyncio

load_dotenv()

token = os.environ["TELEGRAM_BOT_KEY"]
chat_id = os.environ["TELEGRAM_BOT_CHAT_ID"]

bot = telegram.Bot(token)

async def get_history():
    await bot.send_message(chat_id=chat_id, text="Hello")
    
async def main():
    await get_history()

if __name__ == "__main__":
    asyncio.run(main())