class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy=0
        sell=1
        max_profit=0
        while sell<len(prices):
            profit=prices[sell]-prices[buy]
            if prices[buy]<prices[sell]:
                max_profit=max(max_profit,profit)
            else:
                buy=sell
            sell+=1
        return max_profit
obj = Solution()
prices=[1,2,4,2,5,7,2,4,9,0,9]
print(obj.maxProfit(prices))