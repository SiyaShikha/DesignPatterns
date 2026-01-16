from factory.logger.interface import Logger, LoggerFactory

class FileLogger(Logger):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def log(self, message: str) -> None:
        with open(self._file_path, "a", encoding="utf-8") as file:
            file.write(f"{message}\n")
class FileLoggerFactory(LoggerFactory):
    def __init__(self, file_path: str):
        self._file_path = file_path
        
    def create_logger(self):
        return FileLogger(self._file_path)