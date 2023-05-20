This program converts a youtube video to mp3 audio only format and sends it to the preset telegram bot.

To create your own telegram chat bot:
    1) Go to https://t.me/BotFather
    2) After you fill the name of your bot and the url, save the API key to .env file using the following format:
    TELEGRAM_BOT_KEY=<your_telegram_bot_api_key>
    (don't forget to remove <>)
    3) You will also need your chat id, to get one type /start to your bot and also type 2-3 other short messages.
    Then go to:
    https://api.telegram.org/bot<your_telegram_bot_api_key>/getUpdates
    (don't forget to remove <>)
    and copy "id" (not the "message_id" it should be just "id) to your .env file using the following format:
    TELEGRAM_BOT_CHAT_ID=<your_chat_id>
    (don't forget to remove <>)