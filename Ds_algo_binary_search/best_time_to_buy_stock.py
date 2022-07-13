class Solution(object):
    def maxProfit(self, prices):
    #     a=self.buy(prices)
    #     return int(self.sell(prices)-prices[a])
        
        
    # def buy(self,prices):
    #     n=len(prices)
    #     res=prices[0]
    #     for i in range(n):
    #         min(res,prices[i])
    #         # if(res>prices[i]):
    #         #     res=prices[i]
    #     return i
    # def sell(self,prices):
    #     n=len(prices)
    #     b=self.buy(prices)
    #     if(prices[b]==prices[-1]):
    #         return prices[b]
    #     else:
            
    #         res1=prices[b+1]
    #     # b=self.buy(prices)
    #     for j in range(b+1,n):
    #         max(res1,prices[j])
    #         # if(res1<prices[j]  ):
    #         #     res1=prices[j]
    #     return res1
prices=[7,1,5,3,6,4]
a=Solution()
print(a.maxProfit(prices))