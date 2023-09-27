### method1: O(Nk)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummyNode = ListNode(0, None)

        for i in range(len(lists)):
            head = tail = None

            if not dummyNode.next:
                # nodes have not occurred
                p1 = None
            else:
                p1 = dummyNode.next
            p2 = lists[i]

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
                
                if not head:
                    head = currNode
                    tail = currNode
                else:
                    tail.next = currNode
                    tail = tail.next
                
            dummyNode.next = head

        return dummyNode.next


### method2: min heap; O(N*log k)

import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, l))
                l = l.next
        
        dummyNode = ListNode(0, None)
        tail = dummyNode

        while heap:
            tail.next = (heapq.heappop(heap))[1]
            tail = tail.next
        tail.next = None
        return dummyNode.next

        