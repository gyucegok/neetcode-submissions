class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # BFS in a grid, and it's not very different from counting level/depth
        # Multi source BFS??
        from collections import deque

        ROWS, COLS = len(grid), len(grid[0])

        visit = set()
        queue = deque()

        time, fresh = 0, 0

        # Search for the rotten fruit
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
            
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                directions = [(0,1), (0,-1), (1,0), (-1,0)]

                for rd, cd in directions:
                    if (min(r+rd, c+cd) < 0 or r+rd == ROWS or c+cd == COLS or grid[r+rd][c+cd] != 1):
                        continue

                    grid[r+rd][c+cd] = 2
                    fresh -=1
                    queue.append((r+rd, c+cd))

            time += 1

        return time if fresh == 0 else -1


        



        