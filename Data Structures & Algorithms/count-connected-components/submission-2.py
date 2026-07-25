class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)    
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
        res = 0
        for i in range(n):
            if i in visited:
                continue
            res += 1    
            dfs(i, -1)  
        return res              