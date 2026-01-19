from factory.notification.notification import Notification


class SMSNotification(Notification):
    def send(self, msg):
        print(f"Sending SMS: {msg}")