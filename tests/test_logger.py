from logger.console_logger import ConsoleLogger

def test_console_logger_logs_message(capfd):
    logger = ConsoleLogger()
    test_message = "testing console logger"
    logger.log(test_message)

    captured = capfd.readouterr()
    assert f"[Console] {test_message}" in captured.out
