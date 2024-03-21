class Node:
    def __init__(self, url='Home', nxt = None, prev = None) -> None:
        self.url = url
        self.next = nxt
        self.prev  = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = Node(homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        self.curr.next = Node(url, prev = self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        curr = self.curr
        while curr:
            curr = curr.prev
        while steps and self.curr != self.home:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.url

    def forward(self, steps: int) -> str:

        while steps and self.curr and self.curr.next:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)