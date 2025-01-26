# https://leetcode.com/problems/valid-sudoku/solutions/3277043/beats-96-78-short-7-line-python-solution-with-detailed-explanation/

# Beats 96.78 % solutions

class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))