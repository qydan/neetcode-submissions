class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_map = defaultdict(list)
        visiting = set()
        visited = set()

        for course, prereq in prerequisites:
            adj_map[prereq].append(course)

        def dfs(course):
            if course in visiting: # cycle check
                return False
            if course in visited: # already checked and safe
                return True

            visiting.add(course)

            for neighbor in adj_map[course]:
                if not dfs(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
