'''
Created on 5 Jan 2015

@author: Yuan
'''
'''
This problem can be solved by using a dictionary
We first use it to record if the next element appears in the dictionary
In other words, Dic[i] = i+1 in Dic

Then we go through the keys in the dictionary and calculate the number of consecutive numbers from that key.
For each key, we consider Dic[key] as follows:
    1. Dic[key] == True
        there is key+1 in the dictionary, we can continue
    2. Dic[key] == False
        we don't need to continue
    3. Dic[key] = n
        the longest consecutive sequence from key has length n
So we can do this in a depth-first search manner:
    1. while Dic[key] == True
        we do DFS to find the longest sequence from key
        during our procedure we assing Dic[key'] = False for all visited key'
        if we reach some key' s.t. Dic[key'] is a number, then we know that key' has been examined before
            we can stop and add Dic[key']-1 to the current length
        assign the current length to Dic[key]
    2. coneintue with the next key
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if num == None or len(num) == 0:
            return 0
        Dic = {}
        for key in num:
            Dic[key] = key+1 in Dic
            if key-1 in Dic:
                Dic[key-1] = True
        Max = 1
        for key in Dic:
            if Dic[key] == True:
                current = 1
                currentkey = key
                while currentkey in Dic and Dic[currentkey] == True:
                    current += 1
                    Dic[currentkey] = False
                    currentkey += 1
                if currentkey in Dic and type(Dic[currentkey]) == int:
                    current+=Dic[currentkey]-1
                Dic[key] = current
                Max = max(Max, current)
        return Max
    
sol = Solution()
print sol.longestConsecutive([1,0,-1])