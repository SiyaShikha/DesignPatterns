class ConsoleLogger:
    def log(self, message: str) -> None:
        print(f"[Console] {message}")


class ConsoleLoggerFactory:
    def create(self):
        return ConsoleLogger()