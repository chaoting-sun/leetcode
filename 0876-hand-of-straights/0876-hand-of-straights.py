### method1: heap + hashtable

# time complexity: O(NlogN)
# space complexity: O(N)

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) < groupSize or len(hand) % groupSize != 0:
            return False

        heapq.heapify(hand)
        hashTable = defaultdict(int)
        
        for h in hand:
            hashTable[h] += 1
        
        while hand:
            minv = heapq.heappop(hand)
            if minv not in hashTable:
                continue

            for i in range(groupSize):
                k = minv + i
                if k not in hashTable:
                    return False
                hashTable[k] -= 1
                
                if hashTable[k] == 0:
                    hashTable.pop(k)
        
        return len(hand) == 0


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) < groupSize or len(hand) % groupSize != 0:
            return False

        counts = {}
        for h in hand:
            counts[h] = counts.get(h, 0) + 1

        sorted_keys = sorted(list(counts.keys()))

        for k in sorted_keys:
            if counts[k] == 0:
                continue
            
            need = counts[k]
            
            for i in range(groupSize):
                val = k + i
                if val not in counts or counts[val] < need:
                    return False
                counts[val] -= need
        return True