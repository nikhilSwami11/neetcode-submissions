"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        visited = set()
        q = deque()

        q.append(node)
        mp = {node: Node(node.val)}

        while q:
            nd = q.popleft()

            for neig in nd.neighbors:
                if neig not in mp:
                    mp[neig] = Node(neig.val)
                    q.append(neig)
                mp[nd].neighbors.append(mp[neig])
        
        return mp[node]

        

        