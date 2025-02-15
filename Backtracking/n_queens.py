from typing import List


class Solution:
    """
    example on the left: [1, 3, 0, 2]
    example on the right: [2, 0, 3, 1]
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions
        
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state: # [],  
            return range(n) # [0, 1, 2, 3]
        
        # find the next position in the state to populate
        position = len(state) # 1
        candidates = set(range(n)) # {0}
        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)
            dist = position - row
            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return

        candidates = self.get_candidates(state, n)
        for candidate in candidates: # [0, 1, 2, 3], [0]
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()
    
    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret
    
s = Solution()
print(s.solveNQueens(4))

# ["Q...",
#  "....",
#  "....",
#  "...."]

# ["Q...",
#  "....", # [2, 3] # [0, 1, 2, 3] # [2, 3]
#  "....",
#  "...."]

# ["Q...",
#  "....",
#  "....",
#  "...."]

# ["Q...",
#  "...Q",
#  ".Q..",
#  "...."]

# ["Q...",
#  "...Q",
#  "....",
#  "...."]

# ["....",
#  "....",
#  "....",
#  "...."]

# ["....",
#  "....",
#  "....",
#  "...."]

# ["..Q.",
#  "....",
#  "....",
#  "...."]