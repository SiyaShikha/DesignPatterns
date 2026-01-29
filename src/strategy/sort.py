from strategy.sorting_algo import BubbleSort

class Sort:
    def __init__(self, algo):
        self._algo = algo
    def sort(self,arr):
        return self._algo.perform_sort(arr)

# bubble_sorter = BubbleSort()
# arr = [9,0,7,8,70,6,98]
# sorter = Sort(bubble_sorter)
# print(sorter.sort(arr))