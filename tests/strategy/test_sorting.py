from strategy.sort import Sort
from strategy.sorting_algo import BubbleSort


def test_sort():
    a = [1,5,6,78,4]
    bubble_sorter = BubbleSort()
    sorter = Sort(bubble_sorter)
    assert sorter.sort(a) == [1,4,5,6,78]
    