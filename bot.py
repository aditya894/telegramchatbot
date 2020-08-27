import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s',
                   level=logging.INFO)

logger=logging.getLogger(__name__)

TOKEN = "1056264161:AAFCwn0F6nuQw9Eyw2VotCKvObb8WLL73i4"

def start(bot, update):
	print(update)
	author= updater.message.from_user.first_name
	reply= "Hi!{}".format(author)
	bot.send_message(chat_id=update.message.chat_id, text=reply)

def _help(bot, update):
	help_txt= "Hey! This is the help text."
	bot.send_message(chat_id=update.message.chat_id, text=help_txt)


def echo_text(bot, update):
	reply=update.message.text
	bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(bot, update):
	bot.send_sticker(chat_id=update.message.chat_id, sticker=update.message.sticker.file_id)

def error(bot, update):
	logger.error("Update '%s' caused error '%s'",update,update.error)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_Handler(CommandHandler("start",start))
    dp.add_Handler(CommandHandler("help",_help))
    dp.add_Handler(CommandHandler("Filters.text", echo_text))
    dp.add_Handler(CommandHandler("Filters.sticker", echo_sticker))
    dp.add_error_Handler(CommandHandler(error))
    updater.start_polling()
    logger.info("polling started..")
    updater.idle()
    

if __name__ == "__main__":
	main()