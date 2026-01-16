from logger.interface import Logger, LoggerFactory

class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[Console] {message}")


class ConsoleLoggerFactory(LoggerFactory):
    def create(self):
        return ConsoleLogger()