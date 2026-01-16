from factory.logger.console_logger import ConsoleLoggerFactory
from factory.logger.file_logger import FileLoggerFactory


class AppConfig:
    def __init__(self, type, path=None):
        self.type = type
        self.path = path

class Application:
    def __init__(self, config):
        self.logger_factory = self._build_logger_factory(config)

    def _build_logger_factory(self, config):
        if config.type == "console":
            return ConsoleLoggerFactory()
        if config.type == "file":
            return FileLoggerFactory(config.path)

    def logger(self):
        return self.logger_factory.create_logger()


# app_config = AppConfig(type="file", path="./output/test.log")
# app = Application(config=app_config)
# app_logger = app.logger()
# app_logger.log("This is a test message.")