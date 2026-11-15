class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0


        def dfs(row, column):
            if row < 0 or row >= ROWS or column < 0 or column >= COLS or grid[row][column] == 0:
                return 0

            grid[row][column] =  0

            area = 1 
            for direction_row, direction_col in directions:
                area += dfs(row + direction_row, column + direction_col)

            return area            

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] ==  0:
                    continue
                else:
                    max_area = max(max_area, dfs(row, col))

        return max_area