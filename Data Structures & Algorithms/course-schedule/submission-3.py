class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        make an adj
        dfs each course
        dfs
            if course in seen:
                return False
            if not adj[course]:
                return True
            seen.add(course)
            for prereq in adj[course]:
                dfs(prereq)
            seen.remove(course)
            adj[course] = []
            return True          
        '''
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if not adj[course]:
                return True      
            seen.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            adj[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True                    
            