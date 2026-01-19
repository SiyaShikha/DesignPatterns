def test_computer_builder_returns_computer_with_required_components():
    computer = ComputerBuilder().with_cpu('Intel i9').with_ram('32GB').build()
    assert isinstance(computer, Computer)
    assert computer.cpu == 'Intel i9'
    assert computer.ram == '32GB'