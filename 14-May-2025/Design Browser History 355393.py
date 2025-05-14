# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.for_hist = []

    def visit(self, url: str) -> None:
        self.hist.append(url)
        self.for_hist = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.hist) > 1:
            self.for_hist.append(self.hist.pop())
            steps -= 1
        return self.hist[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.for_hist:
            self.hist.append(self.for_hist.pop())
            steps -= 1
        return self.hist[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)