class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:    
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(i, parent):
            if i in visited:
                return
            visited.add(i)
            for neigh in adj[i]:
                if neigh == parent:
                    continue
                dfs(neigh, i)
            return   

        res = 0
        for i in range(n):
            if i in visited:
                continue
            res += 1
            dfs(i, -1)    
        return res