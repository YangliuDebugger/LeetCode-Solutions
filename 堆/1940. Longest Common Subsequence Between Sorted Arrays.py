class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = []
        import heapq
        L = []
        total = len(arrays)
        for i in range(total):
            L.append([arrays[i][0], i, 0])
            arrays[i].append(101)
        heapq.heapify(L)
        last_val = -1
        last_cnt = 0
        while True:
            val, array_idx, ele_idx = heapq.heappop(L)
            if last_val == val:
                last_cnt += 1
            else:
                last_val, last_cnt = val, 1
            if last_cnt == total:
                res.append(last_val)
            # break loop
            if ele_idx == len(arrays[array_idx]) - 1:
                break
            ele_idx += 1
            heapq.heappush(L, [arrays[array_idx][ele_idx], array_idx, ele_idx])
        if res and res[-1] == 101:
            res.pop()
        return res
