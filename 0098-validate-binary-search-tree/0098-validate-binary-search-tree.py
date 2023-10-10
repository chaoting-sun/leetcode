# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### method1: dfs; preorder traversal

# class Solution:
#     def dfs(self, root, minBound, maxBound):
#         if not root:
#             return True
#         if not minBound < root.val < maxBound:
#             return False
#         return self.recursion(root.left, minBound, root.val) \
#            and self.recursion(root.right, root.val, maxBound)

#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.recursion(root, float('-inf'), float('inf'))


### method2: inorder traversal with array

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def inorderTraversal(root, arr):
#             if root:
#                 inorderTraversal(root.left, arr)
#                 arr.append(root.val)
#                 inorderTraversal(root.right, arr)
#             return arr
#         res = inorderTraversal(root, [])
#         for i in range(1, len(res)):
#             if res[i-1] >= res[i]:
#                 return False
#         return True


### method3: inorder traversal with stack

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        minBound = float('-inf')

        while root or len(stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if minBound >= node.val:
                    return False
                else:
                    minBound = node.val
                    root = node.right
        return True
