from builder.computer import Computer


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def with_cpu(self, cpu: str):
        self.cpu = cpu
        return self

    def with_ram(self, ram: str):
        self.ram = ram
        return self

    def with_storage(self, storage: str):
        self.storage = storage
        return self

    def with_gpu(self, gpu: str):
        self.gpu = gpu
        return self

    def build(self):
        if self.cpu is None or self.ram is None:
            raise ValueError("CPU and RAM are required fields")
        return Computer(
            cpu=self.cpu,
            ram=self.ram,
            storage=self.storage,
            gpu=self.gpu
        )
    
    def reset(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        return self