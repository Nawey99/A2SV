# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.pr = []

    def add(self, num: int) -> None:
        if num == 0:
            self.pr = []
        elif len(self.pr) >0:
            self.pr.append(self.pr[-1] * num)
        else:
            self.pr.append(num)
    def getProduct(self, k: int) -> int:
        if len(self.pr)< k:
            return 0
        elif len(self.pr) == k:
            return self.pr[-1]
        else:
            return self.pr[-1]//self.pr[-(k+1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)