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


### method3: merge sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge2Lists(self, l1, l2):
        dummyNode = ListNode(0, None)
        tail = dummyNode
        p1, p2 = l1, l2
        
        while p1 and p2:
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next
        if p1: tail.next = p1
        if p2: tail.next = p2

        return dummyNode.next

    def merge(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        elif l + 1 == r:
            return self.merge2Lists(lists[l], lists[r])
        
        c = l + (r-l)//2

        left = self.merge(lists, l, c)
        right = self.merge(lists, c+1, r)
        return self.merge2Lists(left, right)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.merge(lists, 0, len(lists)-1)

