class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        ans = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            q = deque()
            q.append(i)
            while q:
                curr = q.popleft()
                for neig in adj[curr]:
                    if neig not in visited:
                        q.append(neig)
                        visited.add(neig)
            ans += 1
        return ans