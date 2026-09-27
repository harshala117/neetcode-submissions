from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # 1. Build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        # 2. Find courses that are ready
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # 3. Process courses
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:

                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 4. Cycle check
        if len(order) != numCourses:
            return []

        return order