class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    

        left = 0
        right = 1
        profit = 0
        maxProfit = 0
        while right< len(prices):
            if prices[left]>prices[right]:
                left=right
                
            profit = prices[right]-prices[left]
            right+=1
            

            
            maxProfit = max(maxProfit,profit)

        return maxProfit