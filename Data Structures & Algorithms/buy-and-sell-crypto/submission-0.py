class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] < prices [j]:
                    diff = prices[j] - prices[i]
                    if diff > max_prof:
                        max_prof = diff
        return max_prof
        