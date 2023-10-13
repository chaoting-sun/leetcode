# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        NodeList = []
        curr = head
        while curr:
            NodeList.append(curr)
            curr = curr.next

        tail = curr = NodeList[-1]
        for i in range(len(NodeList)-2, -1, -1):
            curr.next = NodeList[i]
            curr = NodeList[i]
        NodeList[0].next = None
        return tail


        