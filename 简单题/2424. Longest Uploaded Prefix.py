class LUPrefix:

    def __init__(self, n: int):
        self.stream = [0] * (n + 1)
        self.start = 0

    def upload(self, video: int) -> None:
        self.stream[video] = 1

    def longest(self) -> int:
        while self.start + 1 < len(self.stream) and self.stream[self.start + 1] == 1:
            self.start += 1
        return self.start

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()