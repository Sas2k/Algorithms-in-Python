class Sorts():
    """The Main Class containing the sorting algorithms"""

    def __init__(self):
        pass

    def BubbleSort(self, arr: list, reverse: bool = False) -> list:
        """
        Bubble Sort Algorithm
        
        Time Complexity: O(n ^ 2)
        Space Complexity: O(1)

        Keyword arguments:
        arr -- the list to sort : list
        reverse -- make it sort it to largest to smallest : bool

        Return: returns a sorted list
        """
        
        swapped = False
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if swapped == False:
                break
            
        return arr if reverse == False else arr[::-1]
        
    def InsertionSort(self, arr: list, reverse: bool = False) -> list:
        """
        Insertion Sort Algorithm

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Keyword arguments:
        arr -- the list to sort : list
        reverse -- make it sort it to largest to smallest : bool

        return: returns a sorted list
        """

        n = len(arr)

        for i in range(1, n):
            curElement = arr[i]
            j = i - 1

            while j >= 0 and curElement < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1

            arr[j + 1] = curElement

        return arr if reverse == False else arr[::1]

    def _partition(self, arr: list, LeftIndex: int, RightIndex: int):
        "Partitioning function for Quick Sort"

        PivotIndex = RightIndex
        StoreIndex = LeftIndex - 1

        for i in range(LeftIndex, RightIndex):
            if arr[i] <= arr[PivotIndex]:
                StoreIndex += 1
                (arr[i], arr[StoreIndex]) = (arr[StoreIndex], arr[i])

            (arr[i + 1], arr[LeftIndex]) = (arr[LeftIndex], arr[i + 1])

        return StoreIndex + 1
    
    def QuickSort(self, arr: list, leftIndex: int, rightIndex: int, reverse: bool = False) -> list:
        """
        Quick Sort Algorithm

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Keyword arguments:
        arr -- the list to sort : list
        leftIndex -- The Leftmost index in the array
        rightIndex -- The Rightmost index in the array 
        reverse -- make it sort it to largest to smallest : bool

        return: returns a sorted list
        """

        if leftIndex < rightIndex:
            pivotIndex = self._partition(arr, leftIndex, rightIndex)
            self.QuickSort(arr, leftIndex, pivotIndex - 1)
            self.QuickSort(arr, pivotIndex + 1, rightIndex)
        
        return arr if not reverse else arr[::1]