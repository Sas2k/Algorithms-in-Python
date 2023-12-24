"""
- Test Cases for Search Algorithms
"""

from random import randint
from search import Search


search = Search()

testCases = [
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        5,
        4
    ],
    [
        [_ for _ in range(0, 100)],
        50,
        50
    ],
    [
        [_ for _ in range(0, 100)],
        101,
        -1
    ]
]

def test_LinearSearch():
    "Test for Linear Search"

    for case in testCases:
        assert search.LinearSearch(case[0], case[1]) == case[2]

def test_BinarySearch():
    "Test for Binary Search"
    
    for case in testCases:
        assert search.BinarySearch(case[0], case[1]) == case[2]

