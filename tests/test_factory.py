from logger.console_logger import ConsoleLoggerFactory, ConsoleLogger

def test_factory_creates_console_logger():
    factory = ConsoleLoggerFactory()
    logger = factory.create()
    assert isinstance(factory, ConsoleLoggerFactory)
    assert isinstance(logger, ConsoleLogger)

def test_dummy():
    assert True
