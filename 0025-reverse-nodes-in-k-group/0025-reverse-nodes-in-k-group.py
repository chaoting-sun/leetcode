### method1: AC but slow (mine)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        prev = None
        curr = head

        dummy = ListNode(next=head)
        last = dummy

        while True:
            cnt = k
            while cnt and fast:
                fast = fast.next
                cnt -= 1
            if cnt != 0:
                break

            cnt = k 
            while cnt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                cnt -= 1
            
            tmp = last.next
            last.next = prev
            tmp.next = curr
            last = tmp

        return dummy.next


### method2: recursion

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        cnt = k
        for i in range(k):
            if not curr: return head
            curr = curr.next

        curr = head
        prev = None
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head.next = self.reverseKGroup(curr, k)
        return prev