# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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