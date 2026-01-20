from abc import ABC, abstractmethod
from factory.notification.email_notification import EmailNotification
from factory.notification.notification import Notification
from factory.notification.sms_notification import SMSNotification

class Application(ABC):
    def notify(self, msg: str):
        notification = self.create_notification()
        notification.send(msg)

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

class EmailApplication(Application):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSApplication(Application):
    def create_notification(self) -> Notification:
        return SMSNotification()
