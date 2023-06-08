import os
from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    filters,
    CallbackContext,
)

async def forward_to_channel(update: Update, context: CallbackContext):
    message = update.message
    if "#job" in message.text:
        await context.bot.forward_message(chat_id=os.getenv('CHANNEL_ID'), from_chat_id=message.chat_id, message_id=message.message_id)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(os.getenv('BOT_TOKEN')).build()

    # Track messages in chat
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_channel))

    application.run_polling(allowed_updates=Update.MESSAGE)

if __name__ == '__main__':
    main()