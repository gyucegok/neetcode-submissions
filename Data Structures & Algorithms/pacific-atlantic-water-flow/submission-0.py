class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        result = []
        
        ROWS , COLS = len(heights), len(heights[0])
        # Pacific: r < 0 or c < 0
        # Atlantic: r >= ROWS or c >= COLS

        from collections import deque

        def bfs(heights,x,y):
            visit = set()
            queue = deque()

            pacific = False
            atlantic = False

            queue.append((x,y))
            visit.add((x,y))

            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()

                    height = heights[r][c]

                    directions = [(1,0), (-1,0), (0,1), (0,-1)]

                    for dr,dc in directions:
                        row_step, col_step = r+dr, c+dc

                        if (row_step <0 or col_step < 0):
                            pacific = True
                            continue
                        if (row_step >= ROWS or col_step >= COLS):
                            atlantic = True
                            continue

                        if ((heights[row_step][col_step] > height) or min(row_step,col_step) < 0 or row_step == ROWS or col_step == COLS or (row_step,col_step) in visit):
                            continue
                        
                        queue.append((row_step, col_step))
                        visit.add((row_step, col_step))
                
            if pacific == True and atlantic == True:
                return [x,y]
            else:
                return []
        
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                a = bfs(heights,x,y)
                if a != []:
                    result.append(a)
        
        return result

                        
                        


                        

                        
                        












        