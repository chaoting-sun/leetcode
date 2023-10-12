# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### method1: bfs

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rightMost = []
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i == size - 1: rightMost.append(node.val)
        return rightMost


### method2: dfs

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightMost = []

        def dfs(root, depth, rightMost):
            if not root:
                return

            if depth == len(rightMost):
                rightMost.append(root.val)
            
            dfs(root.right, depth+1, rightMost)
            dfs(root.left, depth+1, rightMost)
         
        dfs(root, 0, rightMost)
        return rightMost