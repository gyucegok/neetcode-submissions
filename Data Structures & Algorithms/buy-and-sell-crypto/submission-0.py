class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        global_max = 0

        for i in range(len(prices)):
            curr = prices[i]
            local_max = 0
            for j in range(i+1, len(prices), 1):
                local_max = max(local_max, prices[j] - prices[i])
            global_max = max(local_max, global_max)
        return global_max

        
        