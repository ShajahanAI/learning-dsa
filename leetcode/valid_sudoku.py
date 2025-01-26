from typing import List

# https://leetcode.com/problems/valid-sudoku/

# Passed



#           0   1   2   3   4   5   6   7   8
board =   [["5","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]




# validating rows and columns

# calculating brick combinations


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        possible_combinations = [] # will contain each row, column, brick as an array to validate
        column_combinations = {
            column: list() for column in range(9)
        }


        brick_combination =  {
            3: [],
            6: [],
            9: []
        }

        brick_number = 0
        for row in range(9):
            row_array = board[row]
            possible_combinations.append(row_array)
            
            # calculating brick combinations
            if row // 3 != brick_number:
                # This tells us when we are entering a new row set
                brick_number = row // 3
                possible_combinations.extend(brick_combination.values())
                brick_combination =  {
                    3: [],
                    6: [],
                    9: []
                }

            for brick_index in brick_combination:
                brick_combination[brick_index].extend(row_array[brick_index - 3: brick_index])

            for column in range(9):
                column_combinations[column].append(row_array[column])
        
        possible_combinations.extend(brick_combination.values())
        possible_combinations.extend(column_combinations.values())
        return all([self.isValid(combination) for combination in possible_combinations])

    def isValid(self, combination: List[str]) -> bool:
        combination = [value for value in combination if value.isdigit()]
        return len(combination) == len(set(combination))

sol = Solution()
output = sol.isValidSudoku(board=board)
print(output)