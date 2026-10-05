class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        pacific = set()
        atlantic  = set()

        q = deque()

        def dfs(u,v, visited):
            nonlocal directions
            visited.add((u,v))

            for dr, dc in directions:
                x = u + dr
                y = v + dc
                if 0 <= x< m and 0 <= y < n and heights[x][y] >= heights[u][v] and (x,y) not in visited:
                    dfs(x,y,visited)

        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)
        for j in range(n):
            dfs(0,j,pacific)
            dfs(m-1,j,atlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res
        