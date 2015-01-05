'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
The idea is to find the largest prices[j]- prices[i] for i < j
for that purpose, we need to maintain the current best buy-sell price as bestbuy-bestsell.
then we consider the current price:
1. if the current price < lowest price since bestbuy, then the current price becomes the lowest price since bestbuy
2. else, if the current price > bestsell, then bestsell = current price
3. if the current price - lowest since bestbuy > bestsell - bestbuy, then obviously bestsell = current, and bestbuy = lowest since bestbuy
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None:
            return 0
        if len(prices) <= 1:
            return 0
        bestlow = prices[0]
        besthigh = prices[0]
        nextlow = prices[0]
        for current in prices:
            if current < nextlow:
                nextlow = current
            elif current > besthigh:
                besthigh = current
            if current - nextlow > besthigh - bestlow:
                bestlow = nextlow
                besthigh = current
        return besthigh - bestlow