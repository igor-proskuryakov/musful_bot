# -*- coding: utf-8 -*-

from Objects.sender import Sender


class BadRequest:

    def __init__(self, data):
        text = "Sorry, i can't help you"
        self.method = 'sendmessage'
        self.data = {
            'chat_id': data.chat.id,
            'text': text,
            'reply_to_message_id': data.id
        }


class MessageResponse:
    def __init__(self, update):
        self.type = 'MessageResponse'


class CommandResponse:
    def __init__(self, update):
        self.type = 'CommandResponse'


RESPONSE_MAP = {
    'message': MessageResponse,
    'command': CommandResponse
}


class Response(MessageResponse, CommandResponse, BadRequest):
    def assign_response_type(self, data_type=None):
        response_type = RESPONSE_MAP.get(data_type)
        if response_type:
            return response_type
        return BadRequest

    def make_response(self):
        sender = Sender(self)
        sender.send()

    def __init__(self, data):
        self.response_type = self.assign_response_type(data_type=None)
        print(self.response_type)
        self.response_type.__init__(self, data)
        self.make_response()


