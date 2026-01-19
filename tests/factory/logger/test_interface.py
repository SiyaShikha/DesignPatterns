from factory.logger.interface import Logger, LoggerFactory
from factory.logger.console_logger import ConsoleLoggerFactory


def test_logger_abstract_type():
    factory = ConsoleLoggerFactory()
    logger = factory.create_logger()
    assert isinstance(logger, Logger)

def test_logger_factory_abstract_type():
    factory = ConsoleLoggerFactory()
    assert isinstance(factory, LoggerFactory)