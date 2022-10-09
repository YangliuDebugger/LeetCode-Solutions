class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        while n > 0:
            while self.idx < len(self.encoding) and self.encoding[self.idx] == 0:
                self.idx += 2

            if self.idx >= len(self.encoding):
                return -1

            if self.encoding[self.idx] >= n:
                self.encoding[self.idx] -= n
                # if self.encoding[self.idx] == 0:
                #     self.encoding[self.idx] += 2
                #     return self.encoding[self.idx - 1]
                return self.encoding[self.idx + 1]
            else:
                n -= self.encoding[self.idx]
                self.encoding[self.idx] = 0


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)