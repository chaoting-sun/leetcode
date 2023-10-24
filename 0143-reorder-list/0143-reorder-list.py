# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### method1: container + two pointers

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        container = []
        
        curr = head
        while curr:
            container.append(curr)
            curr = curr.next

        i, j = 0, len(container)-1

        while i < j:
            container[i].next = container[j]
            i += 1
            if i < j:
                container[j].next = container[i]
                j -= 1
        container[j].next = None


### method2: two pointers (fast and slow)

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        curr = head
        secondCurr = prev

        while curr and secondCurr:
            curr_next, secondCurr_next = curr.next, secondCurr.next
            curr.next = secondCurr
            secondCurr.next = curr_next
            curr, secondCurr = curr_next, secondCurr_next