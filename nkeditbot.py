from telegram.ext import Updater, filters, CallbackContext 
from telegram.ext import JobQueue
from telegram.ext import MessageHandler
import telegram

update_queue = JobQueue()
bot = telegram.Bot("tokengoeshere")
updater = Updater(bot=bot, update_queue=update_queue) #Make sure to replace bot and update_queue with the appropriate values for the bot.
# Start the bot
Updater.start_polling(timeout=10, clean=True)

def edit_hashtags(update, context):
    bot = context.bot
    message = update.message
    chat_id = message.chat_id

def handle_message(update, context):
if update.message.text == '/edit_hashtags':
    edit_hashtags(update, context)

message_handler = MessageHandler(filters.text, handle_message)
dispatcher.add_handler(message_handler)


# Prompt the user for the channel and the text to replace
bot.send_message(chat_id=chat_id, text="Enter the username of the channel (e.g. @Kemofure)")
channel = context.bot.wait_for_message(chat_id=chat_id).text
bot.send_message(chat_id=chat_id, text="Enter the text to replace (e.g. #jungle_crow)")
old_text = context.bot.wait_for_message(chat_id=chat_id).text
bot.send_message(chat_id=chat_id, text="Enter the new text (e.g. #Large_billed_crow)")
new_text = context.bot.wait_for_message(chat_id=chat_id).text

    # Get the channel ID
channel_id = bot.get_chat(channel).id

    # Iterate through the messages in the channel
for message in bot.iter_history(channel_id):
        # Check if the message is an image with a caption
        if message.photo and message.caption:
            # Replace the old text with the new text in the caption
            caption = message.caption.replace(old_text, new_text)

            # Edit the caption of the message
            bot.edit_message_caption(chat_id=channel_id, message_id=message.message_id, caption=caption)
