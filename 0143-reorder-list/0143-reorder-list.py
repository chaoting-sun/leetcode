# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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