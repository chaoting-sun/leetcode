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