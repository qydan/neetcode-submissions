from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valid sudoku board -> row and colum dont have same value and 3x3 square dont have same value 
        # stored as a list of list
        rows = len(board)
        columns = len(board[0]) # -> both just equal 9 in this case but in case we get n x n sudoku board or something


        # init set for every row, column, box
        seen_numbers_row = defaultdict(set)
        seen_numbers_col = defaultdict(set)
        seen_numbers_boxes = defaultdict(set)


        for r in range(rows):
            for c in range(columns):
                value = board[r][c]
                box = (r //3, c //3 )

                # skip over empty values
                if value == ".":
                    continue

                else:
                    # is the current number seen anywhere in the seen row, column or box
                    if value in seen_numbers_row[r] or value in seen_numbers_col[c] or value in seen_numbers_boxes[box]:
                        return False
                    # add number to seen
                    else:
                        seen_numbers_row[r].add(value)
                        seen_numbers_col[c].add(value)
                        seen_numbers_boxes[box].add(value)
        return True


