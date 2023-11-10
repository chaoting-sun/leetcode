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

        visited = { k: False for k in adjlist }

        def dfs(adjlist, k, visited, ans):
            ans.append(k)
            visited[k] = True

            for v in adjlist[k]:
                if not visited[v]:
                    dfs(adjlist, v, visited, ans)

        ans = []
        dfs(adjlist, curr, visited, ans)
        return ans