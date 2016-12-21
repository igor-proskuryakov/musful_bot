import requests
from Objects.bot import Bot
import pymongo
import datetime

#
# mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
# db = mongo_client.test
# collection = db.test_collection

token = '<BOT.TOKEN>'
bot = Bot(token)
result = bot.getUpdates(1)


