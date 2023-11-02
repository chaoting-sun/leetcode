# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy

        carry = 0

        while l1 or l2:
            num = carry
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            
            carry, val = divmod(num, 10)
            ptr.next = ListNode(val)
            ptr = ptr.next
        
        if carry:
            ptr.next = ListNode(carry)
        return dummy.next