# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        llist = None
        head = None
        p1, p2 = list1, list2

        while p1 or p2:
            if not p1:
                currNode = p2
                p2 = p2.next
            elif not p2:
                currNode = p1
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    currNode = p1
                    p1 = p1.next
                else:
                    currNode = p2
                    p2 = p2.next
            
            if llist is None:
                llist = currNode
                head = llist
            else:
                llist.next = currNode
                llist = llist.next
        return head