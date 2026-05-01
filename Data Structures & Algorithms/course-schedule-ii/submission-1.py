class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        create adj lsit

        maintain 2 hash sets:
        visited -> we added it to output and seen it
        in_cycle -> we haven't hadded to output but we have seen it (signifying a cycle)
        res = []
        dfs
            if course in cycle:
                return False
            if in visited:
                return True    

            cycle.add(course)
            for each prereq:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for each course:
            if not dfs(course):
                return []
        return res            
        '''

        adj = defaultdict(list)
        for c, p in prerequisites:
            adj[c].append(p)

        visited, cycle = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res                               