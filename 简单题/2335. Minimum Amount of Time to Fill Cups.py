class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cnt = 0
        while sum(amount) != 0:
            amount.sort(reverse=True)
            if amount[1] > 0:
                amount[0] -= 1
                amount[1] -= 1
            else:
                amount[0] -= 1
            cnt += 1
        return cnt

