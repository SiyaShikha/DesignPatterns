from factory.notification.factory import EmailNotificationFactory, SMSNotificationFactory


class NotificationType:
    def __init__(self, type: str):
        self.type = type

class Application:
    def __init__(self, config: NotificationType):
        self.notification_factory = self._build_notification_factory(config)

    def _build_notification_factory(self, config: NotificationType):
        if config.type == "email":
            return EmailNotificationFactory()
        if config.type == "sms":
            return SMSNotificationFactory()
        
    def notify(self):
        return self.notification_factory.create_notification()
