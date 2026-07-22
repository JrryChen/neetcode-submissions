class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        cycle = set()
        def dfs(node, parent):
            if node in cycle:
                return False
            cycle.add(node)    
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            return True

        return dfs(0, -1) and len(cycle) == n                   