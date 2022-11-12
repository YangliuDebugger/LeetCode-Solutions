class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # 就是一道simulation的题目
        # DFS 找bob time
        n = len(amount)
        L = [[] for i in range(n)]
        for s, t in edges:
            L[s].append(t)
            L[t].append(s)

        bob_time = [-1] * n
        alice_visit = [-1] * n

        self.find0 = False

        def BobDFS(val, cnt):
            bob_time[val] = cnt
            if val == 0:
                self.find0 = True
            for nxt in L[val]:
                if not self.find0:
                    if bob_time[nxt] == -1:
                        BobDFS(nxt, cnt + 1)
                        if not self.find0:
                            bob_time[nxt] = -1

        BobDFS(bob, 0)
        self.best = -1000000000000000000000

        # 接下来进行Alice DFS
        def AliceDFS(val, cnt, reward):
            alice_visit[val] = 1
            if cnt == bob_time[val]:
                reward += amount[val] // 2
            elif cnt < bob_time[val] or bob_time[val] == -1:
                reward += amount[val]

            if len(L[val]) == 1 and alice_visit[L[val][0]] == 1:
                self.best = max(self.best, reward)

            for nxt in L[val]:
                if alice_visit[nxt] == -1:
                    AliceDFS(nxt, cnt + 1, reward)

            alice_visit[val] = -1

        AliceDFS(0, 0, 0)
        return self.best



