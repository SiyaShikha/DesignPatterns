from DesignPatterns.src.strategy.sort import Sort
from DesignPatterns.src.strategy.sorting_algo import BubbleSort


def test_sort():
    a = [1,5,6,78,4]
    bubble_sort = BubbleSort()
    sorted_list = Sort(bubble_sort , a)
    assert sorted_list == [1,4,5,6,78]
    