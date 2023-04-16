class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_idx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur_idx + 1]
        self.history.append(url)
        self.cur_idx += 1

    def back(self, steps: int) -> str:
        self.cur_idx = max(self.cur_idx - steps, 0)
        return self.history[self.cur_idx]

    def forward(self, steps: int) -> str:
        self.cur_idx = min(self.cur_idx + steps, len(self.history) - 1)
        return self.history[self.cur_idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)