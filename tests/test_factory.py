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