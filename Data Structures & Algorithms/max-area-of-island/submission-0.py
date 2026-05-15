class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(grid,r,c,visit):

            ROWS, COLS = len(grid), len(grid[0])

            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0):
                return 0
            
            
            visit.add((r,c))

            count=0

            count += dfs(grid,r+1,c,visit)
            count += dfs(grid,r-1,c,visit)
            count += dfs(grid,r,c+1,visit)
            count += dfs(grid,r,c-1,visit)

            count +=1

            return count
        
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = dfs(grid,r,c,visit)
                maxArea = max(maxArea,area)
        
        return maxArea

        

        