class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        # dp problem, first find start at i, what is the optimal

        prize = {}
        pos = []
        for p in prizePositions:
            if p not in prize:
                prize[p] = 0
                pos.append(p)
            prize[p] += 1

        if len(pos) == 1:
            return prize[pos[0]]

        # first iteration, backward
        dp = [0 for i in range(len(pos))]
        cnt = prize[pos[-1]]
        line_end_idx = len(pos) - 1  # record the rightmost index still within this segment
        dp[-1] = cnt
        for i in range(len(pos) - 2, -1, -1):
            cnt += prize[pos[i]]
            while pos[line_end_idx] - k > pos[i]:
                cnt -= prize[pos[line_end_idx]]
                line_end_idx -= 1
            dp[i] = max(dp[i - 1], cnt)

        # 2nd iteration, record set i as end, what is the largest segment, forward
        cnt = prize[pos[0]]
        line_begin_idx = 0
        current_max = cnt + dp[1]
        best = cnt
        for i in range(1, len(pos) - 1):
            cnt += prize[pos[i]]
            while pos[line_begin_idx] + k < pos[i]:
                cnt -= prize[pos[line_begin_idx]]
                line_begin_idx += 1
            best = max(cnt, best)
            current_max = max(current_max, best + dp[i + 1])
        return current_max






