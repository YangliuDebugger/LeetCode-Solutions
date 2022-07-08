class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 看数据规模就是NP-hard的问题，枚举所有可能性
        # 关键是怎么设计bitmask
        # 想到一种，设计k个桶，并且保证前一个桶最小的index一定比后一个桶小
        # 用这种保证没有重复计算
        L = [0] * k
        self.global_min = sum(cookies)

        def enumerate(idx, fill_idx):
            if idx == len(cookies):
                self.global_min = min(self.global_min, max(L))
            else:
                for i in range(0, fill_idx + 1):
                    L[i] += cookies[idx]
                    if i == fill_idx and fill_idx < k - 1:
                        enumerate(idx + 1, fill_idx + 1)
                    else:
                        enumerate(idx + 1, fill_idx)
                    L[i] -= cookies[idx]

        enumerate(0, 0)
        return self.global_min
