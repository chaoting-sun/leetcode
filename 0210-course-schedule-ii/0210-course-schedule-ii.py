# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         courseOrdered = [[] for _ in range(numCourses)]
#         courseReversed = [[] for _ in range(numCourses)]

#         for c1, c2 in prerequisites:
#             courseOrdered[c2].append(c1)
#             courseReversed[c1].append(c2)

#         first = -1
#         for i, c in enumerate(courseReversed):
#             if not c:
#                 first = i
#                 break
#         if first == -1:
#             return []
        
#         ans = []
#         stack = [first]
#         visited = [0] * numCourses

#         while stack:
#             c1 = stack.pop()
#             visited[c1] = 1
#             ans.append(c1)

#             for c2 in courseOrdered[c1]:
#                 if not visited[c2]:
#                     stack.append(c2)

#         if len(ans) == numCourses:
#             return ans
#         return []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for _ in range(numCourses)]
        inDegree = { i: 0 for i in range(numCourses) }

        for c1, c2 in prerequisites:
            courses[c2].append(c1)
            inDegree[c1] += 1
        
        track = []

        while inDegree:
            hasCycle = True

            for c1, deg in inDegree.items():
                if deg == 0:
                    track.append(c1)
                    hasCycle = False
                    for c2 in courses[c1]:
                        inDegree[c2] -= 1
                    inDegree.pop(c1)
                    break
            if hasCycle:
                return []
        return track