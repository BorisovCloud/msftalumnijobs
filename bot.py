import os
import asyncio
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, filters, CallbackContext

def forward_to_channel(update: Update, context: CallbackContext):
    message = update.message
    if "#job" in message.text:
        context.bot.forward_message(chat_id=os.getenv('CHANNEL_ID'), from_chat_id=message.chat_id, message_id=message.message_id)

def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    updater = Updater(bot=bot, update_queue=asyncio.Queue())
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_channel))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
