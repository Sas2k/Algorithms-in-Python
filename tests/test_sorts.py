"""
- Test cases for sorting algorithms
"""

from random import shuffle

from sorts import Sorts

sort = Sorts()

testCases = [
    [x for x in range(0, 100)],
    [x for x in range(100, 0, -1)],
    [x for x in range(1, 100^100)]
]

def test_BubbleSort():
    "Test for Bubble Sort"

    for case in testCases:
        original = case
        shuffle(case)
        out = sort.BubbleSort(case)
        assert original == out, f"Expected {original}, got {out}"

def test_InsertionSort():
    "Test for Insertion Sort"
    
    for case in testCases:
        original = case
        shuffle(case)
        out = sort.InsertionSort(case)
        assert original == out, f"Expected {original}, got {out}"

def test_QuickSort():
    "Test for Quick Sort"

    for case in testCases:
        original = case
        shuffle(case)
        out = sort.QuickSort(case, 0, len(case) - 1)
        assert original == out, f"Expected {original}, for {out}"