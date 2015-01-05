'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
This problem has two solutions. Both of time O(n).
Solution 1 makes use of greedy strategy:
1. first find the best trade in all days, then we have 3 options:
    a. find the 2nd best trade before the 1st best trade
    b. find the 2nd best trade after the 1st best trade
    c. the 1st best trade actually includes a huge price drop that can make it into 2 best trades
2. we only need to calculate these three options and find the biggest one

Solution 2 makes use of dynamic programming:
1. there must be some day i s.t. the 1st best trade happens before day i and 2nd best trade happens after day i
2. we can go from beginning to end to find the best trade before day i
3. we can go from end to beginning to find the best trade after day i
4. the best combination is the solution
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


class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        bestBefore = [0]    # best trade till day i
        bestAfter = [0]     # best trade since day len(prices)-1-i
        result = 0
        if prices == None or len(prices) <2:
            return 0
        
        bestbuy = prices[0]
        bestsell = prices[0]
        lastlow = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < lastlow:
                lastlow = prices[i]
            elif prices[i] > bestsell:
                bestsell = prices[i]
            if prices[i] - lastlow > bestsell- bestbuy:
                bestsell = prices[i]
                bestbuy = lastlow
            bestBefore.append(max(bestBefore[i-1], bestsell-bestbuy))
        
        bestbuy = prices[len(prices)-1]
        bestsell = bestbuy
        nexthigh = bestbuy
        for i in range(1,len(prices)):  # here i is the remaining days
            current = prices[len(prices)-i-1]
            if current > nexthigh:
                nexthigh = current
            elif current < bestbuy:
                bestbuy = current
            if nexthigh - current > bestbuy - bestsell:
                bestbuy = current
                bestsell = nexthigh
            bestAfter.append(max(bestAfter[i-1], bestsell-bestbuy))
            result = max(result, bestAfter[i]+bestBefore[len(prices)-1-i])
        
        return result        

sol = Solution2()

print sol.maxProfit([1,2])
