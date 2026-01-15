from logger.logger import Logger, LoggerFactory
from logger.console_logger import ConsoleLoggerFactory, ConsoleLogger

def test_factory_creates_console_logger():
    factory = ConsoleLoggerFactory()
    logger = factory.create()

    assert isinstance(factory, ConsoleLoggerFactory)
    assert isinstance(logger, ConsoleLogger)

def test_factory_abstract_types():
    factory = ConsoleLoggerFactory()
    logger = factory.create()

    assert isinstance(factory, LoggerFactory)
    assert isinstance(logger, Logger)

def test_console_logger_logs_message(capfd):
    logger = ConsoleLogger()
    test_message = "testing console logger"
    logger.log(test_message)

    captured = capfd.readouterr()
    assert f"[Console] {test_message}" in captured.out
