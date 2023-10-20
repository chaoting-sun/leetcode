### method1: math (greedy)

# schedule the most frequent task first, and fill in the others
# source: https://www.youtube.com/watch?v=siNqiP6tk94
# time complexity: O(N+m); m is the idle time
# space complexity: O(N)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1
        maxValue = max(mp.values())
        maxCount = sum([1 for k, v in mp.items() if v == maxValue])
        time = (n+1) * (maxValue-1) + maxCount
        return max(len(tasks), time)


### method2: heap + queue

# time complexity: O(N+m); m is the idle time
# space complexity: O(N)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1
        
        maxheap = []
        for task, num in mp.items():
            heapq.heappush(maxheap, (-num, task))
        
        time = 0
        waitingList = deque([]) # task name, when can be scheduled next time, left

        while maxheap or waitingList:
            time += 1

            if maxheap:
                negNum, task = heapq.heappop(maxheap)
                negNum += 1
                if negNum < 0:
                    waitingList.append((task, time+n, -negNum))
            
            if waitingList and waitingList[0][1] <= time:
                task, _, num = waitingList.popleft()
                heapq.heappush(maxheap, (-num, task))

        return time