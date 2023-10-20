class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1
        maxValue = max(mp.values())
        maxCount = sum([1 for k, v in mp.items() if v == maxValue])
        time = (n+1) * (maxValue-1) + maxCount
        return max(len(tasks), time)

        