from factory.notification.sms_notification import SMSNotification

def test_sms_notification_type():
    notification = SMSNotification()
    assert isinstance(notification, SMSNotification)

def test_sms_notification_send(capfd):
    notification = SMSNotification()
    test_message = "Hello via SMS"
    notification.send(test_message)
    captured = capfd.readouterr()
    print("captured text",captured)
    assert captured.out == f"Sending SMS: {test_message}\n"