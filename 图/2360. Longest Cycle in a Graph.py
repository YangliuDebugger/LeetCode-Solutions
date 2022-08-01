class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.largest = -1
        color = [0] * len(edges)

        def dfs(idx):
            if color[idx] == 1:
                return
            cnt = 0
            d = {idx: cnt}
            while True:
                if edges[idx] == -1:
                    break
                if color[edges[idx]] == 1:
                    break
                if edges[idx] in d:
                    self.largest = max(self.largest, cnt - d[edges[idx]] + 1)
                    # print(cnt, idx, d)
                    break
                cnt += 1
                d[edges[idx]] = cnt
                idx = edges[idx]

            for i in d:
                color[i] = 1

        for idx in range(len(edges)):
            dfs(idx)
        return self.largest