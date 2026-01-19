from factory.notification.email_notification import EmailNotification
from factory.notification.factory import EmailNotificationFactory, SMSNotificationFactory
from factory.notification.sms_notification import SMSNotification


def test_sms_notification_factory():
    factory = SMSNotificationFactory()
    notification = factory.create_notification()
    assert isinstance(notification, SMSNotification)

def test_email_notification_factory():
    factory = EmailNotificationFactory()
    notification = factory.create_notification()
    assert isinstance(notification, EmailNotification)