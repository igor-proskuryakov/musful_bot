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
    def getUpdates(self, last_update_id=1, params={}):
        timeout = params.get('timeout') or 1000
        method = params.get('method') or 'getupdates'
        json_data = {
            'timeout': timeout,
            'offset': last_update_id + 1
        }
        request = requests.post(API_URL + BOT_TOKEN + method, json=json_data)
        result_json = request.json()
        updates = [{update['update_id']: update['message']} for update in result_json['result']]
        if updates:
            last_update_id = [k for k in updates[-1].keys()][0]
        return last_update_id, updates






        # def getUpdates(self):
        # self.method = 'getupdates'
        # self.json_data = {
        #     'timeout': 1000,
        #     'offset': 648551930
        # }
        # self.request = requests.post(self.request_url + self.method,json=self.json_data)
        # print self.request_url+self.method
        # self.result_json = self.request.json()
        # self.updates = [{update['update_id']: update['message']} for update in self.result_json['result']]
        # return self.updates

    def sendMessage(self):
        self.method = 'sendmessage'
        self.json_data = {
            'chat_id': '187553232',
            'text': 'choose your answer',
            'parse_mode': 'markdown',
            'reply_markup': {
                'inline_keyboard': [[{'text': 'yes', 'url': 'http://ya.ru'}, {'text': 'No', 'url': 'http://ya.ru'}]]
            }
        }

        self.request = requests.post(self.request_url + self.method, json=self.json_data)
