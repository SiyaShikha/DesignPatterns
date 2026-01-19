from abc import ABC, abstractmethod
from factory.notification.notification import Notification
from factory.notification.sms_notification import SMSNotification
from factory.notification.email_notification import EmailNotification

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> 'Notification':
        pass

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()