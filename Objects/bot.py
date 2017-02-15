import requests
import Objects.updates as updates
from multiprocessing import Pool
from globals import API_URL, BOT_TOKEN


def send(update):
    rurl = API_URL + BOT_TOKEN
    update.sendResponse(rurl)
    print('Message sended!')


def checkUpdates(check):
    def checker(self, last_update_id=1, params={}):
        multiproc = params.get('multiprocessing') or False
        try:
            print('Last update ID is: %s' % last_update_id)
            last_updated_id, last_updates = check(self, last_update_id, params)
            if last_update_id != last_updated_id:
                print('You have NEW message!')
                print(last_updates)
                fresh_updates = [updates.Update(update) for update in last_updates]
                if multiproc:  # multiprocessing option
                    with Pool(40) as p:
                        p.map(send, fresh_updates)
                else:  # single process option
                    for fresh_update in fresh_updates:
                        send(fresh_update)
            else:
                print('You have not messages :(')
            if last_update_id:
                checker(self, last_update_id=last_updated_id, params=params)
        except:
            raise Exception('Something wrong!')

    return checker


class Bot():
    def __init__(self):
        self.last_update_id = 1

    @checkUpdates
    def getUpdates(self, last_update_id=1, params=None):
        if params is None:
            params = dict()
        method = 'getupdates'
        timeout = params.get('timeout') or 1000
        limit = params.get('limit') or 1000
        allowed_updates = params.get('allowed_updates') or [
            'message',
            'edited_message',
            'channel_post',
            'edited_channel_post',
            'inline_query',
            'chosen_inline_result',
            'callback_query'
        ]
        json_data = {
            'timeout': timeout,
            'offset': last_update_id + 1,
            'limit': limit,
            'allowed_updates': allowed_updates
        }
        request = requests.post(API_URL + BOT_TOKEN + method, json=json_data)
        result_json = request.json()
        updates = [{update['update_id']: update['message']} for update in result_json['result']]
        if updates:
            last_update_id = max([res['update_id'] for res in result_json['result']])
        return last_update_id, updates
