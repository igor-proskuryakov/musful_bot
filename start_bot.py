import requests
from Objects.bot import Bot
from locals import BOT_TOKEN
from Commands.commands_list import *

token = BOT_TOKEN
bot = Bot(token)
result = bot.getUpdates(1)