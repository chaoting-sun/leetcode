"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originToClone = {}

        cloneHead = Node(-1)
        cloneCurr = cloneHead
        curr = head

        while curr:
            cloneCurr.next = Node(curr.val)
            cloneCurr = cloneCurr.next
            originToClone[curr] = cloneCurr
            curr = curr.next

        cloneCurr = cloneHead.next
        curr = head

        while curr:
            if curr.random:
                cloneCurr.random = originToClone[curr.random]
            cloneCurr = cloneCurr.next
            curr = curr.next
        
        return cloneHead.next