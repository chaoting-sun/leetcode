# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


### method1.0: dfs (recursion)
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:
                return []
            return dfs(root.left)+[root.val]+dfs(root.right)
        return dfs(root)[k-1]


### method1.1: optimized dfs (recursion; TLE)
# source: https://leetcode.com/problems/kth-smallest-element-in-a-bst/solutions/3606533/python-recursion-without-stack-easy/
# time complexity: O(N)
# space comlexity: O(1)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        ans = 0

        def dfs(root):
            nonlocal cnt, ans

            if root.left: dfs(root.left)
            cnt -= 1
            print(root.val, cnt)
            if cnt == 0:
                ans = root.val
                return
            if root.right: dfs(root.right)
        # return dfs(root)
        dfs(root)
        return ans

# or

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            nonlocal k
            if not root:
                return None

            left = inorder(root.left)
            if left:
                return left
            k -= 1
            if k == 0:
                 return root.val
            return inorder(root.right)
        return inorder(root)


### method1.2: dfs (iterative)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []

        node = root
        while node:
            stk.append(node)
            node = node.left
        
        while stk:
            node = stk.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            while node:
                stk.append(node)
                node = node.left
        return -1 # cannot find the node with min. kth value


### method2: binary search
# time complexity: balanced -> O(N); not balanced -> O(N^2)
# space complexity: O(1)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def countNode(root):
            if not root: return 0
            return 1 + countNode(root.left) + countNode(root.right)
        
        cnt = countNode(root.left)
        if cnt + 1 == k:
            return root.val
        elif cnt + 1 > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - cnt - 1)