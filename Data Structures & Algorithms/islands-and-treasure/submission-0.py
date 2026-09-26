class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            i,j,time = q.popleft()
            for u,v in directions:
                x = i+u
                y = j+v
                if 0<= x <m and 0<= y< n and grid[x][y] == 2147483647:
                    grid[x][y] = time + 1
                    q.append((x,y,time+1))
        


                    