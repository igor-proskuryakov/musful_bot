class User():
    def __init__(self, user_info=None, login=None, username=None, userlastname=None, user_id=None):
        self.login = login or user_info.get('username', 'mrsmith')
        self.id = user_id or user_info.get('id', 666)
        self.first_name = username or user_info.get('first_name', 'Mr.')
        self.last_name =  userlastname or user_info.get('last_name', 'Smith')
        self.fullname = self.first_name + ' ' + self.last_name