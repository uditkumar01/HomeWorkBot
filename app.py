import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telegram

from utils import get_pdf

import os

import time

from hand import get_pdf


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    
    update.message.reply_text('Hi, this bot can help you in your homework.\nTo begin with it type "\convert"')

def convert(update, context):
    """Send a message when the command /start is issued."""
    
    update.message.reply_text('Now, please send your txt file.')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help! Use /start to begin.')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def read_pdf(update, context):
    # update.message.reply_text("File" + str(update.message.document.file_id))
    txt_file = context.bot.get_file(update.message.document.file_id)
    txt_file.download(custom_path="text/assignment1.txt")
    update.message.reply_text("This process may take time depending on your your file size...")
    get_pdf('assignment1.txt')
    time.sleep(2)
    update.message.reply_text("Your file is almost ready.")
    message = update.effective_message
    message.chat.send_action(telegram.ChatAction.UPLOAD_DOCUMENT)
    message.reply_document(
        document=open('handwritten.pdf', "rb"),
        caption=("Here is your result file")
        
    )
    os.remove('handwritten.pdf')
    
    

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.environ.get('TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("convert", convert))
    dp.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    dp.add_handler(MessageHandler(Filters.document.txt, read_pdf))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()