from factory.logger.file_logger import FileLogger, FileLoggerFactory


def test_file_logger_factory_creates_file_logger():
    factory = FileLoggerFactory("app.log")
    logger = factory.create_logger()
    assert isinstance(factory, FileLoggerFactory)
    assert isinstance(logger, FileLogger)

def test_file_logger_writes_message(tmp_path):
    log_file = tmp_path / "test.log"
    logger = FileLogger(str(log_file))
    logger.log("Hello")
    assert log_file.read_text() == "Hello\n"

def test_file_logger_appends_messages(tmp_path):
    log_file = tmp_path / "test.log"
    logger = FileLogger(str(log_file))
    logger.log("First message")
    logger.log("Second message")
    assert log_file.read_text() == "First message\nSecond message\n"
