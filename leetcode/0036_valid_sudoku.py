"""
https://leetcode.com/problems/valid-sudoku/
"""
from typing import List


# time complexity: O(n**2)
def is_sudoku_valid(sudoku: List[List[str]]) -> bool:
    memo = {
        "row": {},
        "column": {},
        "square": {}
    }
    sudoku_len = len(sudoku)

    for r in range(sudoku_len):
        for c in range(sudoku_len):
            square_index = (r//3, c//3)
            current = sudoku[r][c]
            if current.isdigit():
                if current in memo["row"].setdefault(r, []) \
                        or current in memo["column"].setdefault(c, []) \
                        or current in memo["square"].setdefault(square_index, []):
                    return False
                else:
                    memo["row"][r].append(current)
                    memo["column"][c].append(current)
                    memo["square"][square_index].append(current)
    return True
