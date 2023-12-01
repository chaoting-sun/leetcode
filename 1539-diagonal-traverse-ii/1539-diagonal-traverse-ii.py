### method1: straightforward (TLE)

# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         ans = []
#         m, n = len(nums), max(len(num) for num in nums)

#         for i in range(m):
#             row = i
#             col = 0
#             while row >= 0 and col < n:
#                 try:
#                     ans.append(nums[row][col])
#                 except:
#                     pass
#                 row -= 1
#                 col += 1

#         for j in range(1, n):
#             row = m-1
#             col = j
#             while row >= 0 and col < n:
#                 try:
#                     ans.append(nums[row][col])
#                 except:
#                     pass
#                 row -= 1
#                 col += 1

#         return ans


### method2: BFS

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        queue = deque([(0,0)])        

        while queue:
            x, y = queue.popleft()
            ans.append(nums[x][y])

            if x + 1 < len(nums) and y == 0:
                queue.append((x+1, y))
            if y + 1 < len(nums[x]):
                queue.append((x, y+1))
        return ans


### method3: hash map
# group the number with the same value of col + row and combine them
# source: https://leetcode.com/problems/diagonal-traverse-ii/solutions/597980/python-two-simple-solutions-dictionary-or-sort-o-n/?envType=daily-question&envId=2023-11-22