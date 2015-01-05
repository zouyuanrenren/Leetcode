'''
Created on 4 Jan 2015

@author: Yuan
'''
'''
In an extreme case, one can buy-sell whenever price raise.
Hence the problem essentially asks for the sum of all the price increases
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        total = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                total += prices[i] - prices[i-1]
        return total
        