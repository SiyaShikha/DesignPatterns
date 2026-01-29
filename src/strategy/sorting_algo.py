from abc import ABC,abstractmethod

class SortingAlgo(ABC):
    @abstractmethod
    def perform_sort(self,arr):
        pass    
    
class BubbleSort(SortingAlgo):
    def perform_sort(self, arr):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break 
        return arr 
    
class SelectionSort(SortingAlgo):
    def perform_sort(self, arr):
        size = len(arr)
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[ind], arr[min_index] = arr[min_index], arr[ind]
        return arr
    
# class InsertionSort:
# class MergeSort:
# class QuickSort:
    
    