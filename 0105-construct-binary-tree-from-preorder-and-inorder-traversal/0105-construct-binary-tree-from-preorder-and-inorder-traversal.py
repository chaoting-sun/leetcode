# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            rootVal = preorder.pop(0)
            inRootId = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder, inorder[:inRootId])
            root.right = self.buildTree(preorder, inorder[inRootId+1:])
            return root
        else:
            return None