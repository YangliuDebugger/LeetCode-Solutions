class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 典型的BFS
        ladder = {}
        n = len(board)
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i % 2 == n % 2:
                    jj = n - 1 - j
                else:
                    jj = j
                cnt = (n - 1 - i) * n + jj + 1
                if board[i][j] != -1:
                    ladder[cnt] = board[i][j]
        visit = set()
        L = [1]
        step = 0
        while L:
            tL = []
            step += 1
            for i in L:
                for j in range(i+1, i+7):
                    if j not in visit:
                        visit.add(j)
                        # 不能加入visit，因为涉及到ladder首尾相连的情况
                        if j in ladder:
                            tL.append(ladder[j])
                        else:
                            tL.append(j)
            if n * n in tL:
                return step
            L = tL
        return -1

