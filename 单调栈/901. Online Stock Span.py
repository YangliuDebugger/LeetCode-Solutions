class StockSpanner:

    def __init__(self):
        # 最早的单调栈的题目
        self.stack = [[99999999, -1]]
        self.cnt = -1

    def next(self, price: int) -> int:
        self.cnt += 1
        while self.stack[-1][0] < price:
            self.stack.pop()
        if self.stack[-1][0] != price:
            self.stack.append([price, self.cnt])
        else:
            self.stack[-1][1] = self.cnt
        return self.cnt - self.stack[-2][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)