from factory.notification.application import Application, EmailApplication, SMSApplication
from factory.notification.email_notification import EmailNotification
from factory.notification.sms_notification import SMSNotification


def test_email_application_creates_email_notification():
    app = EmailApplication()
    notification = app.create_notification()
    assert isinstance(notification, EmailNotification)

def test_sms_application_creates_sms_notification():
    app = SMSApplication()
    notification = app.create_notification()
    assert isinstance(notification, SMSNotification)
