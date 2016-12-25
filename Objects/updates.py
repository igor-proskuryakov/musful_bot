# coding=utf-8
import datetime
from user import User
from message import Message
from response import *




class Update():

    def checkCommand(self, entities):
        if entities['type'] == 'bot_command':
            return True
        else:
            return False



    def __init__(self, update):
#         update = {648552071: {
#     u'date': 1481999836,
#     u'text': u'hi',
#     u'from': {
#         u'username': u'igorproskuryakov',
#         u'first_name': u'Igor',
#         u'last_name': u'Proskuryakov',
#         u'id': 187553232
#     },
#     u'message_id': 197,
#     u'chat': {
#         u'username': u'igorproskuryakov',
#         u'first_name': u'Igor',
#         u'last_name': u'Proskuryakov',
#         u'type': u'private',
#         u'id': 187553232
#     }
# }}
        self.update_id = update.keys()[0]
        self.update = update[self.update_id]
        self.update_dt = datetime.datetime.fromtimestamp(int(self.update['date'])).strftime('%Y-%m-%d %H:%M:%S')
        self.user = User(self.update['from'])
        if 'text' in self.update.keys():
            if (self.update['text'][0] == '/'):
                self.update_type = 'command'
                self.command = self.update['text']
            else:
                self.update_type = 'message'
                self.message = Message(text=self.update['text'], user=self.user, id=self.update['message_id'], chat=self.update['chat'])
        else:
            pass


    #Отправка ответа на сообщение любого типа
    def sendResponse(self, request_url):
        response = newResponse(self)
        response.send(request_url)





