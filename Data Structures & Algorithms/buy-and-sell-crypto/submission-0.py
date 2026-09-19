class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = float("inf")
        best = 0

        for p in prices:
            cheapest = min(cheapest, p)
            best = max(best, p - cheapest)
        return best
        