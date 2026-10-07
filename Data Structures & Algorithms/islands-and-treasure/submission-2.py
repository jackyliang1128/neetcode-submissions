class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ## idea: multisource bfs

        # INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()

        def processCell(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if grid[r][c] == -1:
                return
            
            if (r, c) in visited:
                return
            
            visited.add((r,c))
            queue.append((r,c))


        
        ## append all the gates in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        distance = 0

        while queue:
            currLen = len(queue)
            for i in range(currLen):
                r, c = queue.popleft()


                grid[r][c] = distance

                processCell(r + 1, c)
                processCell(r - 1, c)
                processCell(r, c + 1)
                processCell(r, c - 1)

            distance += 1
        






            
            



        