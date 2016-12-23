import requests
from Objects.bot import Bot
from locals import BOT_TOKEN
from Commands.commands_list import *
import pymongo
import datetime

#
# mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# db = mongo_client.test
# collection = db.test_collection

token = BOT_TOKEN
bot = Bot(token)
result = bot.getUpdates(1)