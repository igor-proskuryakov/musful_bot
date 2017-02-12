import requests
from Objects.bot import Bot
from locals import BOT_TOKEN
from Commands.commands_list import *
from multiprocessing import Pool


token = BOT_TOKEN
bot = Bot()
bot.getUpdates(params={
    'timeout': 1000,
    'multiprocessing': True
})