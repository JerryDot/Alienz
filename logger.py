

class Logger:

    def __init__(self, a_game):
        self.log_message = ''
        self.color = 'green'

    #def add_log_message(self, log_message):
    #    self.log_message.append(log_message)

    def update_log(self, log_message, color='green'):
        self.log_message = log_message
        self.color = color