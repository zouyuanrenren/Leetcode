'''
Created on 30 Dec 2014

@author: Yuan
'''

'''
The idea is to use a greedy strategy, starting from the child with least rating, examine each child:
1. if the child has a left neighbour whose rating is lower, then it gets 1 more candy than the left neighbour
2. if the child has a right neighbour whose rating is lower, then it gets 1 more candy than the right neighbour, or remain same, whichever more
3. otherwise, the child gets 1 candy.

So we can first sort all child index based on their rating and then apply the greedy strategy.
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
        