from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        number_of_islands = 0


        def bfs(start_row, start_col):

            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = "0"

            while queue:
                row, col = queue.popleft()
                for direction_row, direction_col in directions:

                    new_row, new_col = row + direction_row, col + direction_col

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == "1":

                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = "0"

        for row in range(ROWS):

            for col in range(COLS):

                if grid[row][col] == "0":
                    continue
                    
                else:
                    bfs(row, col)
                    number_of_islands += 1

        return number_of_islands

                