# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### method1: slow and fast; two pointers

# slow pointer -> turtle; fast point -> rabbit
# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # when the rabbit meet the turtle
            if slow == fast:
                return True
        return False

### method2: set

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False