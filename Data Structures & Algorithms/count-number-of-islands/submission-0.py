class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # bfs
        q = deque()
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    while q:
                        i1,j1 = q.popleft()
                        for u,v in directions:
                            x = i1 + u
                            y = j1+ v
                            if 0 <= x < m and 0<= y < n and grid[x][y] == "1" and (x,y) not in visited:
                                q.append((x,y))
                                visited.add((x,y))
                    island+=1
        return island
                    

