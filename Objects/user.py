class User():
    def __init__(self, user_info=None, login=None, username=None, userlastname=None, user_id=None):
        if user_info:
            self.login = getattr(user_info, 'username', None)
            self.id = user_info['id']
            self.first_name = getattr(user_info, 'first_name', None)
            self.last_name = getattr(user_info, 'last_name', None)
            self.fullname = self.first_name + ' ' + self.last_name
        else:
            self.login = login
            self.id = user_id
            self.first_name = username
            self.last_name = userlastname
            self.fullname = self.first_name + ' ' + self.last_name

