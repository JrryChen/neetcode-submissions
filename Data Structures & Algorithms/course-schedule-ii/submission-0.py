class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        course_map = defaultdict(list)

        for course, prereq in prerequisites:
            course_map[course].append(prereq)

        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prereq in course_map[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res                       