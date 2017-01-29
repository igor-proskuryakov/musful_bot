# -*- coding: utf-8 -*-

import requests
from Commands.commands_list import *


def sendResponse(response_url, method, json_data):
    request = requests.post(response_url + method, json=json_data)
    return True


class BadRequest():
    def send(self, response_url):
        pass

    def __init__(self, update):
        self.method = 'sendmessage'
        pass


class MessageResponse():
    def send(self, response_url):
        sendResponse(response_url, self.method, self.json_data)

    def responseToMessage(self):
        self.method = 'sendmessage'
        self.message_text = u'Hello, ' + self.response_to.fullname + '!' + \
                            u'\nSend me /start command for more information.'
        self.json_data = {
            'chat_id': self.response_to.id,
            'text': self.message_text
        }
        return True

    def __init__(self, update):
        self.response_to = update.user
        self.type = 'MessageResponse'
        self.update = update
        self.responseToMessage()


class CommandResponse:
    def send(self, response_url):
        sendResponse(response_url, self.method, self.json_data)

    def responseToCommand(self):
        self.method = 'sendmessage'
        self.command = getCommand(self.update.command, self.update)
        self.json_data = self.command.response

        return True

    def __init__(self, update):
        self.type = 'CommandResponse'
        self.response_to = update.user
        self.update = update
        self.responseToCommand()


def newResponse(update):
    responses = {
        'command': CommandResponse,
        'message': MessageResponse
    }
    if not getattr(update, 'update_type', None) or getattr(update, 'update_type', None) not in responses:
        return BadRequest(update)
    else:
        return responses[update.update_type](update)
