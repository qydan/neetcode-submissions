from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        order = []

        

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1



        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

    
        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in adj_list[current]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []