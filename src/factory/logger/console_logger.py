from factory.logger.interface import Logger, LoggerFactory

class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[Console] {message}")


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self):
        return ConsoleLogger()