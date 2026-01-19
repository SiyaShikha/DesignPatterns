from factory.notification.email_notification import EmailNotification


def test_email_notification_type():
    notification = EmailNotification()
    assert isinstance(notification, EmailNotification)

def test_email_notification_send(capfd):
    notification = EmailNotification()
    test_message = "Hello via Email"
    notification.send(test_message)
    captured = capfd.readouterr()
    assert captured.out == f"Sending Email: {test_message}\n"