from factory.notification.sms_notification import SMSNotification

def test_sms_notification_type():
    notification = SMSNotification()
    assert isinstance(notification, SMSNotification)