import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

def forward_to_channel(update: Update, context: CallbackContext):
    message = update.message
    if "#job" in message.text:
        context.bot.forward_message(chat_id=os.getenv('CHANNEL_ID'), from_chat_id=message.chat_id, message_id=message.message_id)

def main():
    updater = Updater(token=os.getenv('BOT_TOKEN'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), forward_to_channel))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()