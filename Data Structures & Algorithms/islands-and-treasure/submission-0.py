class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # Multi Source BFS
        from collections import deque

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visit.add((i,j))
                    queue.append((i,j))

        length = 0

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 2147483647:
                    grid[r][c] = length

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for rd,cd in directions:
                    if (min(r+rd,c+cd) < 0 or r+rd == ROWS or c+cd == COLS or grid[r+rd][c+cd] == -1 or (r+rd,c+cd) in visit):
                        continue
                    
                    visit.add((r+rd,c+cd))
                    queue.append((r+rd,c+cd))
            length += 1
        return



