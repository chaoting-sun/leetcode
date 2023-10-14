### method1: dfs (TLE)

# time complexity: O(E+V^2) (?)
# space complexity: O(E+V)

class Solution:
    def isCyclic(self, courses, c, visited):
        if visited[c]:
            return True
        
        visited[c] = True
        for i in courses[c]:
            if self.isCyclic(courses, i, visited):
                return True
        visited[c] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        visited = [False] * numCourses

        for a, b in prerequisites:
            courses[b].append(a)

        for i in range(numCourses):
            if self.isCyclic(courses, i, visited):
                return False
        return True


### method2: dfs + coloring algorithm

# intuition: For a node, if all of its child nodes have been visited and found no cycles. Next time if this node are found from the other nodes, we can pass it.
# source: https://leetcode.com/problems/course-schedule/solutions/658275/c-dfs-easiest-solution-with-explanation-my-1st-approach/?envType=list&envId=rab78cw1

# time complexity: O(E+V)
# space complexity: O(E+V)

class Solution:
    def isCyclic(self, courses, c, visited):
        if visited[c] == 1:
            return True
        if visited[c] == 2:
            return False

        for i in courses[c]:
            visited[c] = 1 # its current childs are being visited
            if self.isCyclic(courses, i, visited):
                return True
        visited[c] = 2 # all of the childs of the node have been visited
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        visited = [0] * numCourses

        for a, b in prerequisites:
            courses[b].append(a)

        for i in range(numCourses):
            if self.isCyclic(courses, i, visited):
                return False
        return True


### more: https://leetcode.com/problems/course-schedule/?envType=list&envId=rab78cw1