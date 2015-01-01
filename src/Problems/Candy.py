'''
Created on 30 Dec 2014

@author: Yuan
'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        od = sorted(range(len(ratings)), key = lambda x:ratings[x])
        candies = [0]*len(ratings)
        for index in od:
            candies[index] = 1
            if index > 0 and ratings[index] > ratings[index-1]:
                candies[index] = candies[index-1]+1
            if index < len(ratings) -1 and ratings[index] > ratings[index+1]:
                candies[index] = max(candies[index], candies[index+1]+1)
        return sum(candies)
    
sol = Solution()

print sol.candy([1, 2, 6, 2, 5,4,1])
        