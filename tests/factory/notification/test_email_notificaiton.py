from factory.notification.email_notification import EmailNotification


def test_email_notification_type():
    notification = EmailNotification()
    assert isinstance(notification, EmailNotification)