from telegram.ext import Updater, filters, CallbackContext
from telegram.ext import JobQueue
from telegram.ext import MessageHandler
import telegram

update_queue = JobQueue()
bot = telegram.Bot("5811307345:AAGtbmrYWbf3lkyZonrr1ZH83e9w7tm9dG8")
updater = Updater(bot=bot, update_queue=update_queue)
updater.start_polling(poll_interval=0.0, timeout=10, bootstrap_retries=-1, read_timeout=2, write_timeout=None, connect_timeout=None, pool_timeout=None, allowed_updates=None, drop_pending_updates=None, error_callback=None)

def edit_hashtags(update, context):
    # Use the update object to access the chat_id and the bot object
    chat_id = update.message.chat_id
    bot = context.bot

    # Prompt the user for the channel and the text to replace
    bot.send_message(chat_id=chat_id, text="Enter the username of the channel (e.g. @Kemofure)")
    channel = update.message.text
    bot.send_message(chat_id=chat_id, text="Enter the text to replace (e.g. #jungle_crow)")
    old_text = update.message.text
    bot.send_message(chat_id=chat_id, text="Enter the new text (e.g. #Large_billed_crow)")
    new_text = update.message.text

    # Get the channel ID
    channel_id = bot.get_chat(channel).id

    # Print the values of the variables to check if they are what you expect
    print(f"channel: {channel}")
    print(f"old_text: {old_text}")