from logger.console_logger import ConsoleLogger
from logger.console_logger import ConsoleLoggerFactory

def test_console_factory_creates_console_logger():
    factory = ConsoleLoggerFactory()
    logger = factory.create()

    assert isinstance(factory, ConsoleLoggerFactory)
    assert isinstance(logger, ConsoleLogger)

def test_console_logger_logs_message(capfd):
    logger = ConsoleLogger()
    test_message = "testing console logger"
    logger.log(test_message)
    captured = capfd.readouterr()
    assert captured.out == f"[Console] {test_message}\n"


def test_console_logger_logs_empty_message(capfd):
    logger = ConsoleLogger()
    test_message = ""
    logger.log(test_message)
    captured = capfd.readouterr()
    assert captured.out == f"[Console] \n"
