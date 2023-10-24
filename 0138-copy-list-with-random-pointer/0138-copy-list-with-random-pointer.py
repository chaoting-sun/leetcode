"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

### method: 2 pass (hash map)

# source: https://leetcode.com/problems/copy-list-with-random-pointer/solutions/258935/detailed-explanation-with-pictures-c-javascript/?envType=list&envId=rr2ss0g5
# method: copy the llist in the first traversal, and construct a hashmap from each original node to the corresponding new node. To add the random pointer, we first reach the random pointer from each node in the original llist and use the hashmap to get the new node.

# time complexity: O(N)
# space complexity: O(N)

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


### optimization - make the space complexity O(1)

# add new nodes in the original llist, in which each new node is at the right side of the cloned node. then, the random pointer of each new node is the next node of the random pointer of its previous node.

# time complexity: O(N)
# space complexity: O(1)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        while curr:
            cloneCurr = Node(curr.val, curr.next)
            curr.next = cloneCurr
            curr = cloneCurr.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        cloneHead = head.next
        cloneCurr = cloneHead

        while cloneCurr.next:
            cloneCurr.next = cloneCurr.next.next
            cloneCurr = cloneCurr.next
        
        return cloneHead