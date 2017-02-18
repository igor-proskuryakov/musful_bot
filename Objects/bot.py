import requests
import Objects.updates as upd
from multiprocessing import Pool
from globals import REQUEST_URL, ALL_UPDATES_TYPES
import json


class Bot():
    def __init__(self, last_update_id=1, multiprocessing=False, pool_size=20):
        self.last_update_id = last_update_id
        self.multiprocessing = multiprocessing
        self.pool_size = pool_size

    def response_all(self):
        pass

    def get_updates(self, last_update_id=1, timeout=1000, limit=50,
                    allowed_updates=ALL_UPDATES_TYPES):
        method = 'getupdates'
        json_data = {
            'timeout': timeout,
            'offset': self.last_update_id + 1,
            'limit': limit,
            'allowed_updates': allowed_updates
        }
        print(json_data)
        request = requests.post(REQUEST_URL + method, json=json_data)
        result_json = request.json()
        with open('debug.txt', 'a') as debug:
            json.dump(result_json, debug)
        updates = [upd_data for upd_data in result_json['result']]
        if updates:
            self.last_update_id = max([res['update_id'] for res in result_json['result']])
            print(self.last_update_id)
            updates = [upd.get_update_type(update) for update in updates]
        return updates
