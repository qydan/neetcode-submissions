class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)] # caridnal directions
        rows = len(grid)
        columns = len(grid[0])
        fresh_fruit_count = 0
        queue = collections.deque()
        minutes = 0

        for row in range(rows):
            for column in range(columns):

                curr_fruit = grid[row][column]

                if curr_fruit == 0: # skip if 0
                    continue

                elif curr_fruit == 1:
                    fresh_fruit_count += 1

                else:
                    queue.append((row, column))

        if fresh_fruit_count == 0:
            return 0

        # bfs search starting from initial rotten fruit -> prepopulated queue via the double for loo

        while fresh_fruit_count > 0 and queue:

            for _ in range(len(queue)):
                row, column = queue.popleft()

                for direction_row, direction_column in directions:
                    new_row, new_column = row + direction_row, column + direction_column
                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == 1:
                        grid[new_row][new_column] = 2
                        fresh_fruit_count -= 1
                        queue.append((new_row, new_column))

            minutes += 1

        return minutes if fresh_fruit_count == 0 else -1




            
