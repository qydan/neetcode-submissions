from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        in_degree = [0] * numCourses
        order = []


        for course, prereq in prerequisites:
            adj_map[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque()
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            order.append(current)
            
            for neighbor in adj_map[current]: # for every course that had the current course as a prereq
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
