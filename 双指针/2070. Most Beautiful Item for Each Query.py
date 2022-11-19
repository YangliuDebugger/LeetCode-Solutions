class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = [[val, idx] for idx, val in enumerate(queries)]
        queries.sort()
        res = [0] * len(queries)
        items_idx = 0
        queries_idx = 0
        current_max_beauty = 0
        while queries_idx < len(queries):
            max_price, map_idx = queries[queries_idx]
            while items_idx < len(items) and items[items_idx][0] <= max_price:
                current_max_beauty = max(current_max_beauty, items[items_idx][1])
                items_idx += 1
            res[map_idx] = current_max_beauty
            queries_idx += 1
        return res