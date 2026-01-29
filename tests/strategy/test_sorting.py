from strategy.sort import Sort
from strategy.sorting_algo import BubbleSort, SelectionSort


def test_bubble_sort():
    a = [1,5,6,78,4]
    bubble_sorter = BubbleSort()
    sorter = Sort(bubble_sorter)
    assert sorter.sort(a) == [1,4,5,6,78]

def test_selection_sort():
    a = [1,5,6,78,4]
    selection_sorter = SelectionSort()
    sorter = Sort(selection_sorter)
    assert sorter.sort(a) == [1,4,5,6,78]
    