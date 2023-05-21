import os
import logging
from dotenv import load_dotenv
import utils
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, 
    ContextTypes, 
    CommandHandler,
)

# load env variables
load_dotenv()


# token for telegram bot
telegram_token = os.environ["TELEGRAM_BOT_KEY"]


# logging format
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This handler sends back a welcoming message to a user.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=utils.WELCOMING_MESSAGE
    )


async def youtube_convert(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    This handler converts a youtube video (via provided link) to an mp3 format audio and sends it back.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Please wait."
    )

    url = context.args[0]
    file_name = utils.download_youtube_audio(url, utils.PATH_TO_DOWNLOADS)
    path_to_mp4 = utils.PATH_TO_DOWNLOADS + "/" + file_name + ".mp4"
    path_to_mp3 = utils.PATH_TO_DOWNLOADS + "/" + file_name + ".mp3"
    utils.convert_mp4_to_mp3(path_to_mp4, path_to_mp3)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Downloading complete."
    )

    await context.bot.send_audio(
        chat_id=update.effective_chat.id,
        audio=path_to_mp3
    )


async def delete_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This handler deletes all files in the Downloads folder from the server.
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Deleting files, please wait..."
    )
    
    utils.delete_files()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Files deleted."
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    youtube_handler = CommandHandler('youtube', youtube_convert)
    delete_handler = CommandHandler('delete', delete_files)

    application.add_handler(start_handler)
    application.add_handler(youtube_handler)
    application.add_handler(delete_handler)

    application.run_polling()
