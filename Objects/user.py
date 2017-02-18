class User:
    def __init__(self, user_info):
        self.login = user_info.get('username')
        self.id = user_info.get('id')
        self.first_name = user_info.get('first_name')
        self.last_name = user_info.get('last_name')
        self.fullname = self.first_name + ' ' + self.last_name