### method: hash table

# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        
        for p1, p2 in adjacentPairs:
            adjlist[p1].append(p2)
            adjlist[p2].append(p1)
        
        for k, v in adjlist.items():
            if len(v) == 1:
                curr = k
                break

        def dfs(adjlist, prev, curr, ans):
            ans.append(curr)

            for v in adjlist[curr]:
                if v != prev:
                    dfs(adjlist, curr, v, ans)
                    break

        ans = []
        dfs(adjlist, float('-inf'), curr, ans)
        return ans