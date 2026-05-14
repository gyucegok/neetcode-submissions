class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0,1
        maxP = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                maxP = max(maxP, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return maxP


        

# Solution 1: Brute Force
#        global_max = 0

#        for i in range(len(prices)):
#            curr = prices[i]
#            local_max = 0
#            for j in range(i+1, len(prices), 1):
#                local_max = max(local_max, prices[j] - prices[i])
#            global_max = max(local_max, global_max)
#        return global_max

        
        