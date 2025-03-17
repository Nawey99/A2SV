# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        res = [0] * n
        que = deque()
        for i in range(n):
            que.append(i)
        for i in range(n):
            res[que[0]] = deck[i]
            que.popleft()
            if que:
                x = que.popleft()
                que.append(x)
        return res