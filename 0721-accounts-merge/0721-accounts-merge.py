### method1: dfs; hashmap

# time complexity: O(# emails + len(accounts))
# space complexity: O(# emails + len(accounts))

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


### method2: union find

# source: https://www.youtube.com/watch?v=6st4IxEF-90

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i

        accountToEmails = defaultdict(list)
        for e, i in emailToAccount.items():
            leader = uf.find(i)
            accountToEmails[leader].append(e)
        
        res = []
        for i, emails in accountToEmails.items():
            name = accounts[i][0]
            res.append([name]+sorted(emails))
        return res