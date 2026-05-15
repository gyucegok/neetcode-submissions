class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()

        def dfs(grid, r, c, visit):
            ROWS,COLS = len(grid), len(grid[0])

            if (min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0' or (r,c) in visit):
                return 0

            visit.add((r,c))

            dfs(grid,r+1,c,visit)
            dfs(grid,r-1,c,visit)
            dfs(grid,r,c+1,visit)
            dfs(grid,r,c-1,visit)

            return 1
        
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count += dfs(grid,r,c,visit)
        
        return count








        