class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack =[]
        adj = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if adj[course] == []:
                return True

            seen.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            adj[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True                                        