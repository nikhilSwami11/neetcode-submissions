class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set()
        q = deque()

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        max_len = 0

        for i in range(m):
            for j in range(n):
                count = 0
                if grid[i][j] == 1 and (i,j) not in visited:
                    q.append((i,j))
                    visited.add((i,j))
                    count +=1
                    while q:
                        x1,y1 = q.popleft()
                        for u,v in directions:
                            x = x1 + u
                            y = y1 + v
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x,y) not in visited:
                                q.append((x,y))
                                visited.add((x,y))
                                count += 1
                    max_len = max(max_len, count)
        return max_len


                    