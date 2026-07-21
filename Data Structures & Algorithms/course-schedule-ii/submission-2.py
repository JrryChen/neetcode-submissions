class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        create adj matrix
        explored set of those we already fully explored the branch
        cycle set to make sure we don't reexplore the same node
        '''

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        output = []
        explored = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in explored:
                return True
            cycle.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            explored.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output                                  