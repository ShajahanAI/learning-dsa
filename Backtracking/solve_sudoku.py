from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solutions = []
        state = set()
        self.search(state, solutions)
        

    def is_valid_state(self, state: List[tuple[int, int, str]]):
        # check if it is a valid solution
        return len([i for i in state if i[-1].isdigit()]) == 9 * 9

    def get_candidates(self, state):
        candidates = set(range(1, 10))
        


    def search(self, state, solutions):
        if self.is_valid_state(state):
            solutions.append(state.copy())
            # convert to board # TODO
            # return

        for candidate in self.get_candidates(state):
            state.add(candidate)
            self.search(state, solutions)
            state.remove(candidate)




[["5","3","4","6","7","8","9","1","2"],
 ["6","7","2","1","9","5","3","4","8"],
 ["1","9","8","3","4","2","5","6","7"],
 ["8","5","9","7","6","1","4","2","3"],
 ["4","2","6","8","5","3","7","9","1"],
 ["7","1","3","9","2","4","8","5","6"],
 ["9","6","1","5","3","7","2","8","4"],
 ["2","8","7","4","1","9","6","3","5"],
 ["3","4","5","2","8","6","1","7","9"]]

[(0, 0, 5), (0, 1, 3), (0, 2, 4)] # (row_index, column_index, value)

[(0, 0, candidate)] # candidate -> x in {1 - 9}
