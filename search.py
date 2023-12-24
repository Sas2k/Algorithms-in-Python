class Search():
    """Main Search Algorithms Class"""

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
    
    def BinarySearch(self, arr: list, target) -> int:
        """
        Binary Search Algorithms

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Keyword arguments:
        arr -- the list to find stuff.
        target -- the thing to find.

        Return: the index of the target if found or if not found returns -1
        """

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

        return -1