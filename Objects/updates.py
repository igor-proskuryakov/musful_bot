# coding=utf-8
import datetime
from Objects.user import User
from Objects.message import Message
from Objects.response import *
from globals import REQUEST_URL
from globals import ALL_UPDATES_TYPES


# Класс оставлен для возможного будущего наследования
# class Update():
#     def __init__(self, update):
#         self.update_id = update['update_id']

class MessageUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
            self.message = Message(update['message'])
            self.update = update
        except:
            raise Exception('Update params not founded!')


class EditedMessageUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


class ChannelPostUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


class EditedChannelPostUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


class InlineQueryUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


class ChosenInlineResultUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


class CallbackQueryUpdate():
    def __init__(self, update):
        try:
            self.update_id = update['update_id']
        except:
            raise Exception('Update params not founded!')


def get_update_type(update):
    if update.get('message'):
        return MessageUpdate(update)
    elif update.get('edited_message'):
        return EditedMessageUpdate(update)
    elif update.get('channel_post'):
        return ChannelPostUpdate(update)
    elif update.get('edited_channel_post'):
        return EditedChannelPostUpdate(update)
    elif update.get('inline_query'):
        return InlineQueryUpdate(update)
    elif update.get('chosen_inline_result'):
        return ChosenInlineResultUpdate(update)
    elif update.get('callback_query'):
        return CallbackQueryUpdate(update)
    else:
        raise Exception('Not founded update type!')
