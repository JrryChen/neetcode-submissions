class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, origin, parent):
            # return true means we need to remove edge that we originated from
            if node == origin and parent != -1:
                return True
            for neigh in adj[node]:
                if neigh == parent:
                    continue 
                if dfs(neigh, origin, node):
                    return True
            return False               

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            if dfs(a, a, -1):
                return [a, b]