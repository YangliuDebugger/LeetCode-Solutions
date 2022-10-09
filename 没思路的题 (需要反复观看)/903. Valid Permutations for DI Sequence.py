class Solution:
    def numPermsDISequence(self, s: str) -> int:
        # 数据规模可以到O(n^3)
        # 还是可以变成dp的题目
        # 这是一个二维dp，dp[m][n] 记录前m个数字以n结尾有多少种可能性
        # 难点在于好像是有后效性的，怎么保证前面用到的数字后面不再被考虑

        # 看了 https://leetcode.com/problems/valid-permutations-for-di-sequence/solutions/168278/c-java-python-dp-solution-o-n-2/
        # 的解答发现了是状态划分的问题，第一维的状态是对的，第二维的状态不那么容易想到