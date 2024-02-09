from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def send_message(self, mail, message):
        pass


class HangoutMessage(Message):
    def send_message(self, mail, message):
        print('Send {} to {}'.format(message, mail))


class WhatsAppMessage(Message):
    def send_message(self, phone_no, message):
        print('Send {} to {}'.format(message, phone_no))


hangout_message = HangoutMessage()
hangout_message.send_message('test@gmail.com', 'hello')

whatapp_message = WhatsAppMessage()
whatapp_message.send_message('987731793', 'hello')