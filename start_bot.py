from Objects.bot import Bot
from locals import BOT_TOKEN

token = BOT_TOKEN
bot = Bot()
bot.getUpdates(params={
    'timeout': 1000,
    'multiprocessing': True
})