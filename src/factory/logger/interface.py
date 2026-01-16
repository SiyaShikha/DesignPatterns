from abc import ABC, abstractmethod 

class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass