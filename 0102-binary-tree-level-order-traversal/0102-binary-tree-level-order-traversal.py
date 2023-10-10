# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### method1: preorder traversal + additional array

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
            

### method2: queue

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
        
        