from Objects.chat import Chat
from Objects.user import User


class Message():
    def _assign_command(self, entities):
        self.is_command = True

    def __init__(self, message):
        self.id = message.get('message_id') or None
        self.user = User(message.get('from'))
        self.date = message.get('date')
        self.chat = 'Chat()'
        self.text = message.get('text')
        self.is_command = None
        self._entities = message.get('entities')
        if self._entities and [e for e in self._entities if e.get('type') == 'bot_command']:
            self._assign_command()
