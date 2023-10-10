# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### method1: preorder traversal + additional array

# time complexity: O(nlogn)
# space complexity: O(n)

# class Solution:
#     def preorderTraversal(self, root, level, arr):
#         if root:
#             arr.append((root.val, level))
#             self.preorderTraversal(root.left, level+1, arr)
#             self.preorderTraversal(root.right, level+1, arr)

#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         arr = []
#         self.preorderTraversal(root, 0, arr)
#         arr.sort(key=lambda x: x[1])

#         ans = []
#         l = 0
#         i = 0
#         while i < len(arr):
#             tmp = []
#             while i < len(arr) and arr[i][1] == l:
#                 tmp.append(arr[i][0])
#                 i += 1
#             ans.append(tmp)
#             l += 1
#         return ans


### method2: preorder traversal (optimized)


# time complexity: O(nlogn)
# space complexity: O(n)

# class Solution:
#     def preorderTraversal(self, root, level, ans):
#         if not root: return
#         if level == len(ans):
#             ans.append([])

#         ans[level].append(root.val)
#         self.preorderTraversal(root.left, level+1, ans)
#         self.preorderTraversal(root.right, level+1, ans)

#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         ans = []
#         self.preorderTraversal(root, 0, ans)
#         return ans


### method2: queue (first in first out)

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = [root]

        while len(queue):
            size = len(queue)

            tmp = []
            while size:
                root = queue.pop(0)
                tmp.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
                size -= 1
            ans.append(tmp)
        return ans
        
        