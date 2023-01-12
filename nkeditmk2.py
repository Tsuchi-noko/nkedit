import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

bot = telegram.Bot("5811307345:AAGtbmrYWbf3lkyZonrr1ZH83e9w7tm9dG8")
updater = Updater(bot=bot, update_queue=5)

def main():
    updater.start_polling(poll_interval=0.0, timeout=10, bootstrap_retries=-1, read_timeout=2, write_timeout=None, connect_timeout=None, pool_timeout=None, allowed_updates=None, drop_pending_updates=None, error_callback=None)
main()

def start(update, context):
    update.message.reply_text("Bot started.")

def edit_channel(update, context):
    # Get the channel's username from the user
    channel_username = update.message.text.split()[1]
    if not channel_username.startswith("@"):
        update.message.reply_text("Please provide a valid channel username (i.e. one that starts with '@').")
        return

    # Get the channel's id
    channel_id = None
    try:
        channel = bot.get_chat(channel_username)
        channel_id = channel.id
    except telegram.TelegramError as e:
        update.message.reply_text("Could not find channel {}. Error: {}".format(channel_username, e))
        return
    # check if bot is admin in channel or not
    if not channel.get_member(bot.id).status in ['administrator','creator']:
        update.message.reply_text("Bot not have permission to edit message in this channel.")
        return
    
    # Ask the user for the text to edit
    update.message.reply_text("Please provide the text that you want to edit.")
    context.user_data["channel_id"] = channel_id
    return "text_to_edit"

def text_to_edit(update, context):
    text_to_edit = update.message.text
    context.user_data["text_to_edit"] = text_to_edit
    update.message.reply_text("Please provide the text which you want to replace with.")
    return "edited_text"

def edited_text(update, context):
    edited_text = update.message.text
    text_to_edit = context.user_data["text_to_edit"]
    channel_id = context.user_data["channel_id"]

    # Ask for confirmation before proceeding
    update.message.reply_text("Please confirm, you want to replace {} with {}?".format(text_to_edit, edited_text))
    context.user_data["edited_text"] = edited_text
    return "confirmation"

def confirmation(update, context):
    if update.message.text.lower() in ["yes", "y"]:
        channel_id = context.user_data["channel_id"]
        edited_text = context.user_data["edited_text"]
        text_to_edit = context.user_data["text_to_edit"]
        # Edit messages in the channel
        for msg in bot.iter_history(channel_id):
            if msg.text.find(text_to_edit) != -1:
                bot.edit_message_text(edited_text,channel_id, msg.message_id)
        update.message.reply_text("All matching text has been replaced.")
    else:
        update.message.reply_text("Aborted.")
    return ConversationHandler.END
