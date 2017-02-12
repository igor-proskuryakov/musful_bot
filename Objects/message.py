from Objects.chat import Chat


class Message():
    def __init__(self, text=None, user=None, id=None, chat=None):
        self.text = text
        self.user = user
        self.id = id
        self.chat = Chat(chat_type=chat['type'], user=self.user)
        pass