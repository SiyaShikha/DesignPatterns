class DatabaseConnection:
    _instance = None

    def __init__(self):
        self.connected = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("Creating new database connection...")
            cls._instance = cls()
        return cls._instance