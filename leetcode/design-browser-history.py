class Node(object):
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        node = Node(homepage)
        self.head = node
        self.cur = node

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        node = Node(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node

        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        i = 0
        while i < steps and self.cur.prev:
            self.cur = self.cur.prev
            i += 1
        return self.cur.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        i = 0
        while i < steps and self.cur.next:
            self.cur = self.cur.next
            i += 1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)