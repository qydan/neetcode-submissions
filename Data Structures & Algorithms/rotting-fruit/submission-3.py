from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        ROWS = len(grid) 
        COLS = len(grid[0])
        minutes = 0
        queue = deque()
        fresh_fruit_count = 0


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0: # skip 0s in the grid
                    continue
                elif grid[row][col] == 2: # seed any starting points (rotten fruit) in our BFS queue
                    queue.append((row, col))
                else:
                    fresh_fruit_count += 1

        while fresh_fruit_count > 0 and queue: # BFS queue
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for direction_row, direction_col in directions:
                    new_row, new_column = row + direction_row, col + direction_col

                    if 0 <= new_row < ROWS and 0 <= new_column < COLS and grid[new_row][new_column] == 1:
                        fresh_fruit_count -= 1
                        grid[new_row][new_column] = 2
                        queue.append((new_row, new_column))

            minutes += 1

                

        return minutes if fresh_fruit_count == 0 else -1