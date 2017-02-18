from locals import BOT_TOKEN

BOT_TOKEN += '/'
API_URL = 'https://api.telegram.org/bot'
REQUEST_URL = API_URL + BOT_TOKEN
ALL_UPDATES_TYPES = [
    'message',
    'edited_message',
    'channel_post',
    'edited_channel_post',
    'inline_query',
    'chosen_inline_result',
    'callback_query'
]