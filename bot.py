from setuptools import Command
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from currency_exchange import *


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = '5535149674:AAF7GYGADEXoIjJCxVhjU-n4JmNMdVxVikM'


def start(update, context):
    update.message.reply_text(f'{result}')


def help(update, context):
    update.message.reply_text("Help")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(
        BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('rate', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
