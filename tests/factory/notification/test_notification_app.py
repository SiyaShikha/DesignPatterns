from factory.notification.app import Application, NotificationType
from factory.notification.email_notification import EmailNotification
from factory.notification.sms_notification import SMSNotification


def test_app_email_notification():
    config = NotificationType(type="email")
    app = Application(config=config)
    notification = app.notify()
    assert isinstance(notification, EmailNotification)

def test_app_sms_notification():
    config = NotificationType(type="sms")
    app = Application(config=config)
    notification = app.notify()
    assert isinstance(notification, SMSNotification)