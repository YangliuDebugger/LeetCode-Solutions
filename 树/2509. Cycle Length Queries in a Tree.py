class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # for each query, we need to find least old ancestor
        @cache
        def find_common(i, j, cnt):
            if i > j:
                i, j = j, i
            if i == j:
                return cnt
            return find_common(j // 2, i, cnt + 1)

        res = [1 + find_common(i, j, 0) for i, j in queries]
        return res

