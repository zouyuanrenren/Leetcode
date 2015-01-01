'''
Created on 30 Dec 2014

@author: Yuan
'''
from string import lower

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None:
            return 0
        time = [0,len(prices)]
        profit = self.maxPro(prices,time)
        profit1 = self.maxPro(prices,[0,profit[0]])
        profit2 = self.maxPro(prices,[profit[1]+1,len(prices)])
        newprices = prices[profit[0]:profit[1]]
        newprices = newprices[::-1]
        profit3 = self.maxPro(newprices, [0,len(newprices)])
        return profit[2]+max(profit1[2], profit2[2], profit3[2])
    
    def maxPro(self,prices,time):
        if(time[1] <= time[0]):
            return [0,0,0]
        nextlow = time[0]
        bestlow = time[0]
        besthigh = time[0]
        for i in range(time[0],time[1]):
            if prices[i] > prices[besthigh]:
                besthigh = i
            elif prices[i] < prices[nextlow]:
                nextlow = i
            if prices[i] - prices[nextlow] > prices[besthigh] - prices[bestlow]:
                bestlow = nextlow
                besthigh = i
        return [bestlow, besthigh, prices[besthigh]-prices[bestlow]]

sol = Solution()

print sol.maxProfit([6,1,3,2,4,7])