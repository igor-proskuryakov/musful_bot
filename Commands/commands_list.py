COMMANDS = [
    '/start',
    '/help',
    '/currency',
]


class StartCommand():
    def __init__(self, update):
        self.command_response = 'Hello, '+ update.user.fullname + '\ngiYou can choose one from the following commands:\n'
        for command in COMMANDS:
            self.command_response += command + '\n'
        self.response = {
            'chat_id': update.user.id,
            'text': self.command_response
        }



class HelpCommand():
    def __init__(self, update):
        self.command_response = 'You try to use HELP command'
        self.response = {
            'chat_id': update.user.id,
            'text': self.command_response
        }



class CurrencyCommand():
    def __init__(self, update):
        self.command_response = 'You try to use CURRENCY command'
        self.response = {
            'chat_id': update.user.id,
            'text': self.command_response
        }



class UnknownCommand():
    def __init__(self, update):
        self.response = 'Invalid command :( Please try again!'
        self.response = {
            'chat_id': update.user.id,
            'text': 'Invalid command :( Please try again!'
        }


COMMANDS_LIST = {
    '/start': StartCommand,
    '/help': HelpCommand,
    '/currency': CurrencyCommand,
}


def getCommand(command, update):
    print command
    for row in COMMANDS_LIST.keys():
        if row == command:
            return COMMANDS_LIST[command](update)
        else:
            pass
    else:
        return UnknownCommand(update)
