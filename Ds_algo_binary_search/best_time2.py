# def buy(prices):
#     n=len(prices)
#     res=prices[0]
#     for i in range(n):
#         if(res>prices[i]):
#             res=prices[i]
#             a=i
#     return a

# prices=[7,1,5,3,6,4]
# a=buy(prices)
# print(a)
class Solution(object):
    def maxProfit(self, prices):
        for i in range(len(prices) - 1):
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
        # i=0
        # buy=0
        # sell=0
        # profit=0
        # n=len(prices)-1
        # while(i<n):
        #     while(i<n and prices[i+1]<=prices[i]):
        #         buy=prices[i]
        #         i+=1
        #     while(i<n and prices[i+1]>prices[i]):
        #         sell=prices[i]
        #         i+=1
        #     profit+=sell-buy
        # return profit    

prices=[7,1,5,3,6,4]
a=Solution()
print(a.maxProfit(prices))