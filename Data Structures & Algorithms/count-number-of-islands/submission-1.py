from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # so we have a 2d grid
        directions = [(1,0), (-1,0), (0,1), (0,-1)] 
        rows = len(grid)
        columns = len(grid[0])
        number_of_islands = 0


        def bfs(start_row, start_column): 
            queue = deque()
            queue.append((start_row, start_column)) # (0, 1)
            grid[start_row][start_column] == "0"


            while queue:
                row, column = queue.popleft() # 0, 1

                for direction_row, direction_column in directions:
                    new_row, new_column = row + direction_row, column + direction_column

                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == "1": # new traversed row, column is found to be land
                        queue.append((new_row, new_column))
                        grid[new_row][new_column] = "0"

        for row in range(rows):
            for column in range(columns):
                # two cases -> 0 or we have a 1
                if grid[row][column] == "0":
                    continue # skip over 0s
                else:
                    bfs(row, column) # 0, 1
                    number_of_islands +=1

        return number_of_islands