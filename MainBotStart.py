from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from FailingBot.CommandBot import *

bot = Bot(token = '5931424673:AAHvDu8YrD0zNlu8uGhwa87RekXrFhESuvM')
updater = Updater(token = '5931424673:AAHvDu8YrD0zNlu8uGhwa87RekXrFhESuvM')
dispatcher = updater.dispatcher




start_handler = CommandHandler("Hello", start)
abv_handler =  MessageHandler(Filters.text, abv)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(abv_handler)



updater.start_polling()
updater.idle()