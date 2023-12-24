<h3 align="center">Algorithms on Python</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🤖 Algorithms ](#-algorithms-)
  - [Sorting Algorithms \[`sorts.py`\] (`/tests/test_sorts.py`)](#sorting-algorithms-sortspy-teststest_sortspy)
  - [Searching Algorithms \[`search.py`\] (`/tests/test_search.py`)](#searching-algorithms-searchpy-teststest_searchpy)
- [🧪 Testing](#-testing)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

This repository contains implementations of algorithms in python.

## 🤖 Algorithms <a name = "algorithms"></a>

### Sorting Algorithms [`sorts.py`] (`/tests/test_sorts.py`)

| Algorithm      | Time-Complexity | Space-Complexity |
| :------------- | :-------------- | :--------------- |
| Bubble Sort    | O(n^2)          | O(1)             |
| Insertion Sort | O(n^2)          | O(1)             |
| Selection Sort | O(n^2)          | O(1)             |


### Searching Algorithms [`search.py`] (`/tests/test_search.py`)

| Algorithm      | Time-Complexity | Space-Complexity |
| :------------- | :-------------- | :--------------- |
| Linear Search  | O(n)            | O(1)             |
| Binary Search  | O(log n)        | O(1)             |

## 🧪 Testing

Use the following settings in `settings.json` for VSCode to run tests.
```json
{
...
"python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

> NOTE: The tests are written using `pytest`, and works best in VSCodes Test Interface than in the terminal.

## ✍️ Authors <a name = "authors"></a>

- [@Sas2k](https://github.com/Sas2k) - Idea & Initial work

See also the list of [contributors](https://github.com/Sas2k/Algos-in-Py/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- References:
  - https://www.geeksforgeeks.org
  - https://www.programiz.com/