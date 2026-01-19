from factory.logger.app import AppConfig, Application
from factory.logger.console_logger import ConsoleLoggerFactory
from factory.logger.file_logger import FileLoggerFactory


def test_app_console_logger_factory():
    app_config = AppConfig(type="console")
    app = Application(config=app_config)
    assert isinstance(app.logger_factory, ConsoleLoggerFactory)

def test_app_file_logger_factory():
    app_config = AppConfig(type="file", path="./output/test.log")
    app = Application(config=app_config)
    assert isinstance(app.logger_factory, FileLoggerFactory)