import pytest
from builder.computer_builder import ComputerBuilder
from builder.computer import Computer


def test_computer_builder_returns_computer_with_required_components():
    computer = ComputerBuilder().with_cpu('Intel i9').with_ram('32GB').build()
    assert isinstance(computer, Computer)
    assert computer.cpu == 'Intel i9'
    assert computer.ram == '32GB'

def test_computer_builder_raises_error_when_required_components_missing():
    builder = ComputerBuilder().with_ram('16GB')
    with pytest.raises(ValueError):
        builder.build()

def test_computer_builder_includes_optional_components():
    computer = (ComputerBuilder()
                .with_cpu('AMD Ryzen 7')
                .with_ram('16GB')
                .with_storage('1TB SSD')
                .with_gpu('NVIDIA RTX 3060')
                .build())
    assert computer.storage == '1TB SSD'
    assert computer.gpu == 'NVIDIA RTX 3060'

def test_computer_builder_reset_functionality():
    builder = ComputerBuilder()
    computer1 = builder.with_cpu('Intel i7').with_ram('16GB').build()
    assert computer1.cpu == 'Intel i7'
    assert computer1.ram == '16GB'

    builder.reset()

    computer2 = builder.with_cpu('AMD Ryzen 5').with_ram('8GB').build()
    assert computer2.cpu == 'AMD Ryzen 5'
    assert computer2.ram == '8GB'
    assert computer2.storage is None