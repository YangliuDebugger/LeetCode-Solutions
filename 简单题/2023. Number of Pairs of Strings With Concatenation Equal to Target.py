class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # 数据规模这么小？？
        cnt=0
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if idx1 == idx2:
                    continue
                if i +j == target:
                    cnt += 1
        return cnt