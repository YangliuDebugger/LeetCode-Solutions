# https://www.1point3acres.com/bbs/thread-971930-1-1.html

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # BFS
        visit = set()
        seq = board[0] + board[1]
        zero_idx = 0
        for idx, i in enumerate(seq):
            if i == 0:
                zero_idx = idx
        Q = [(seq, zero_idx)]
        step = 0

        moving_map = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

        visit.add(tuple(seq))

        while Q:
            if (1, 2, 3, 4, 5, 0) in visit:
                return step
            step += 1
            tQ = []
            for s, z_idx in Q:
                for move in moving_map[z_idx]:
                    news = s[:]
                    news[z_idx], news[move] = news[move], news[z_idx]
                    if tuple(news) not in visit:
                        tQ.append([news, move])
                        visit.add(tuple(news))
            Q = tQ
        return -1
