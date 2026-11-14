from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list) # defautl dictionary to store the courses and a list of its prerequisites
        number_of_prereqs = [0] * numCourses # store the number of prerequisites for the courses 

        for course, prereq in prerequisites:
            prereq_map[prereq].append(course)
            number_of_prereqs[course] += 1 

        queue = deque()

        for i in range(numCourses):
            if number_of_prereqs[i] == 0:
                queue.append(i)

        courses_taken = 0

        while queue:

            current = queue.popleft()
            courses_taken += 1


            for neighbor in prereq_map[current]:
                number_of_prereqs[neighbor] -= 1
                if number_of_prereqs[neighbor] == 0: queue.append(neighbor)
        
        return courses_taken == numCourses
            
        