class Search():
    """The Main Class containing the search algorithms"""

    def __init__(self):
        pass

    def LinearSearch(self, arr: list, target) -> int:
        """
        Linear Search Algorithm

        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Keyword arguments:
        arr -- the list to find stuff.
        target -- the thing to find.

        Return: the index of the target if found or if not found returns -1
        """
        TargetIndex = -1

        for n in range(0, len(arr)):
            if arr[n] == target:
                TargetIndex = n

        return TargetIndex
    
    def BinarySearch(self, arr: list, target, left = 0, right = -1) -> int:
        """
        Binary Search Algorithms

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Keyword arguments:
        arr -- the list to find stuff.
        target -- the thing to find.
        left -- the first index
        right -- the last index

        Return: the index of the target if found or if not found returns -1
        """

        arr.sort()

        left = 0
        right = len(arr) - 1

        while right >= left:
            mid = int(left + (right - left) / 2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            print(arr[mid])

        return -1
    
    def ExponentialSearch(self, arr: list, target) -> int:
        """
        Exponential Search Algorithm

        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Keyword arguments:
        arr -- the list to find stuff.
        target -- the thing to find.

        Return: the index of the target if found or if not found returns -1
        
        """

        arr.sort()

        if arr[0] == target:
            return 0
        
        i = 1

        while i < len(arr) and arr[i] <= i:
            i *= 2
            print(i)

        return self.BinarySearch(arr, target,  i // 2, min(i, len(arr) - 1))
