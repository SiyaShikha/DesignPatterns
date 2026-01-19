from factory.notification.notification import Notification


class EmailNotification(Notification):
    def send(self, msg):
        print(f"Sending Email: {msg}")
