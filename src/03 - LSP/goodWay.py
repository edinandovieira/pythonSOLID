from abc import ABC, abstractmethod

"""
Liskov Substitution Principle(LSP)

subtype/child class instance should be substitutable for its base class without affecting program
"""

class Message(ABC):
    @abstractmethod
    def send_message(self, mail, message):
        pass


class HangoutMessage(Message):
    def __init__(self, mail):
        self.mail = mail

    def send_message(self, message):
        print('Send {} to {}'.format(message, self.mail))


class WhatsAppMessage(Message):
    def __init__(self, phone_no):
        self.phone_no = phone_no

    def send_message(self, message):
        print('Send {} to {}'.format(message, self.phone_no))


class Person:
    def __init__(self, name, mail, phone_no):
        self.name = name
        self.mail = mail
        self.phone_no = phone_no


class MessageManager:
    def __init__(self, message_obj: Message):
        self.message_obj = message_obj

    def send(self, message):
        self.message_obj.send_message(message)


if __name__ == '__main__':
    person = Person('Dabid', 'dabid@gmail.com', '813908120')
    whatApp_message = WhatsAppMessage(person.phone_no)
    hangout_message = HangoutMessage(person.mail)

    message_manager = MessageManager(whatApp_message)
    message_manager.send('Hello Dabid')

    message_manager.message_obj = hangout_message
    message_manager.send('Hello Dabid')