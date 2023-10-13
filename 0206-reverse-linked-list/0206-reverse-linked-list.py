# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### method1: use an array to store the nodes and traverse the node list twice

# time complexity: O(N)
# space complexity: O(N)

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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prevNode = None
        currNode = head
        nextNode = head.next

        while nextNode:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
        currNode.next = prevNode
        return currNode

