import requests
import updates




def checkUpdates(check):
    def checker(self, last_update_id):
            last_update_id = self.last_update_id
            print ('Last update ID is: %s' % last_update_id)
            check(self, last_update_id)
            if last_update_id != self.last_update_id:
                print ('You have NEW message!')
                print (self.last_updates)
                fresh_updates = [updates.Update(update) for update in self.last_updates]
                for fresh_update in fresh_updates:
                    fresh_update.sendResponse(self.request_url)
            else:
                print ('You have not messages :(')
            if check:
                checker(self, last_update_id)
            return Exception
    return checker




class Bot():
    def __init__(self, token):
        self.api_url = 'https://api.telegram.org/bot'
        self.token = token
        self.request_url = self.api_url + self.token + '/'
        self.last_update_id = 1






    @checkUpdates
    def getUpdates(self, last_update_id):
        method = 'getupdates'
        json_data = {
            'timeout': 1000,
            'offset': last_update_id + 1
        }
        request = requests.post(self.request_url + method, json=json_data)
        result_json = request.json()
        updates = [{update['update_id']: update['message']} for update in result_json['result']]
        if updates:
            self.last_update_id = updates[-1].keys()[0]
            self.last_updates = updates or None
        return True







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
        self.json_data  = {
            'chat_id': '187553232',
            'text': 'choose your answer',
            'parse_mode': 'markdown',
            'reply_markup': {
                'inline_keyboard': [[{'text': 'yes', 'url': 'http://ya.ru'},{'text': 'No', 'url': 'http://ya.ru'}]]
                }
            }

        self.request = requests.post(self.request_url + self.method, json=self.json_data)

