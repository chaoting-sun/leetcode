# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


### method1: two-pass with a dummy node

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(next=head)
        curr = dummy
        nMove = length - n

        while nMove:
            curr = curr.next
            nMove -= 1
        
        curr.next = curr.next.next
        return dummy.next


### method2: one-pass with a hash table

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        dummy = ListNode(next=head)
        curr = dummy

        while curr:
            nodes.append(curr)
            curr = curr.next
        nodes[-n-1].next = nodes[-n].next
        return dummy.next