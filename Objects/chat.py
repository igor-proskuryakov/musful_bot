class Chat():
    def __init__(self, chat_type=None, user=None):
        self.chat_type = chat_type
        self.user = user
        self.id = self.user.id