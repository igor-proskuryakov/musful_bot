from Objects.user import User

ALLOWED_CHAT_TYPES = [
    'private',
    'group'
]


class Chat():
    def __init__(self, chat):
        self.type = chat.get('type') if chat.get('type') in ALLOWED_CHAT_TYPES else 'no_type'
        self.owner = None
        self.title = None
        if self.type != 'private':
            self.title = chat.get('title')
        self.id = chat.get('id')
        self.all_members_are_administrators = chat.get('all_members_are_administrators', False)

    def assign_owner(self, user):
        self.owner = user
        self.title = 'private with %s' % user.login
