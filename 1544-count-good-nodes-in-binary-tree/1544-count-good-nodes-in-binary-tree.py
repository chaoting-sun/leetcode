# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### method1: dfs

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxValue):
            good = 0
            if node.val >= maxValue:
                maxValue = max(node.val, maxValue)
                good = 1

            nLeftGood = nRightGood = 0
            if node.left: nLeftGood = dfs(node.left, maxValue)
            if node.right: nRightGood = dfs(node.right, maxValue)
            
            return nLeftGood + good + nRightGood

        return dfs(root, float('-inf'))


### method2: bfs

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        nGoods = 0
        q = deque([(root, float('-inf'))])

        while q:
            size = len(q)

            for i in range(size):
                node, maxValue = q.popleft()

                maxValue = max(node.val, maxValue)

                if node.val == maxValue:
                    nGoods += 1

                if node.left: q.append((node.left, maxValue))
                if node.right: q.append((node.right, maxValue))
        
        return nGoods