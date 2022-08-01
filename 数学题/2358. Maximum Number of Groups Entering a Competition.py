class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # 贪心
        # (1 + t) * t // 2
        f = int((len(grades) * 2) ** 0.5) + 1
        # print(f)
        while (1+f) * f // 2 > len(grades):
            f -= 1
        return f