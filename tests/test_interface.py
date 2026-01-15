from logger.logger_interface import Logger, LoggerFactory
from logger.console_logger import ConsoleLoggerFactory


def test_logger_abstract_types():
    factory = ConsoleLoggerFactory()
    logger = factory.create()
    assert isinstance(logger, Logger)

def test_logger_factory_abstract_types():
    factory = ConsoleLoggerFactory()
    assert isinstance(factory, LoggerFactory)