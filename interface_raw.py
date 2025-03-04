from abc import ABC, abstractmethod

class NotificationSender(ABC):

    @abstractmethod
    def send(self, mesage: str) -> None:
        pass

class EmailNotificationSender(NotificationSender):

    def send(self, message: str) -> None:
        print(f'Email message - {message}')

class SMSNotificationSender(NotificationSender):

    def send(self, message: str) -> None:
        print(f'SMS message - {message}')


class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        # Validação de dados
        self.__notification_sender.send(message)

obj = Notificator(SMSNotificationSender())
obj.send('Ola Mundo')