# -*- coding: utf-8 -*-

import requests
from Commands.commands_list import *

class Response():
    def sendResponse(self):
        request = requests.post(self.bot + self.method, json=self.json_data)
        return True




    def badRequest(self):
        pass


    def responseToMessage(self):
        self.method = 'sendmessage'
        self.message_text = u'Hello, '+self.response_to.fullname+'!' + \
            '\nYou can try:' + \
            '\n/dollar'
        self.json_data = {
            'chat_id': self.response_to.id,
            'text': self.message_text
        }
        self.sendResponse()
        return True




    def responseToCommand(self):
        self.method = 'sendmessage'
        self.command = getCommand(self.update.command, self.update)
        self.json_data = self.command.response
        self.sendResponse()
        return True






    def __init__(self, bot, update):
        self.bot = bot
        self.response_to = update.user
        self.responce_type = update.update_type
        self.update = update
        if self.responce_type == 'message':
            self.responseToMessage()
        elif self.responce_type == 'command':
            self.responseToCommand()
        else:
            self.badRequest()