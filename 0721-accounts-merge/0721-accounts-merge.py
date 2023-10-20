class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                mp[accounts[i][j]].append(i)
        
        def dfs(email, visited, mp, ans):
            ans[-1].append(email)
            visited[email] = True

            for i in mp[email]:
                for j in range(1, len(accounts[i])):
                    if not visited[accounts[i][j]]:
                        dfs(accounts[i][j], visited, mp, ans)

        ans = []        
        visited = { email: False for email, _ in mp.items() }

        for email, ids in mp.items():
            if not visited[email]:
                ans.append([accounts[ids[0]][0]])
                dfs(email, visited, mp, ans)

        for i in range(len(ans)):
            ans[i] = [ans[i][0]] + sorted(ans[i][1:])

        return ans