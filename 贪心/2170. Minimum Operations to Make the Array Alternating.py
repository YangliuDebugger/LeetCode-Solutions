class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # two hash
        dsame = {}
        ddiff = {}
        for idx, i in enumerate(nums):
            if idx % 2 == 0:
                if i not in dsame:
                    dsame[i] = 0
                dsame[i] += 1
            else:
                if i not in ddiff:
                    ddiff[i] = 0
                ddiff[i] += 1

        a = [(dsame[i], i) for i in dsame]
        b = [(ddiff[i], i) for i in ddiff]

        a.sort(reverse=True)
        b.sort(reverse=True)
        # 处理边界条件
        a.append((0, 1))
        a.append((0, 1))
        b.append((0, 1))
        b.append((0, 1))
        if a[0][1] != b[0][1]:
            return len(nums) - a[0][0] - b[0][0]
        return min(len(nums) - a[0][0] - b[1][0], len(nums) - a[1][0] - b[0][0])
    