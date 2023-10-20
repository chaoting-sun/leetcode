### method: dfs; hashmap

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_acc_map = defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                em_acc_map[accounts[i][j]].append(i)
        
        def dfs(email, visited, em_acc_map, ans):
            ans[-1].append(email)
            visited[email] = True

            for i in em_acc_map[email]:
                for j in range(1, len(accounts[i])):
                    if not visited[accounts[i][j]]:
                        dfs(accounts[i][j], visited, em_acc_map, ans)

        ans = []        
        visited = { em: False for em, _ in em_acc_map.items() }

        for em, ids in em_acc_map.items():
            if not visited[em]:
                ans.append([accounts[ids[0]][0]])
                dfs(em, visited, em_acc_map, ans)

        for i in range(len(ans)):
            ans[i] = [ans[i][0]] + sorted(ans[i][1:])

        return ans