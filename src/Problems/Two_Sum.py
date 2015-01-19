'''
Created on 22 Nov 2014

@author: zouyuanrenren
'''
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
An efficient solution to this problem is to use a hash table:
1. for numbers[i], save in table[numbers[i]] = [...,i+1]
2. then iterate the table, for each key in table, find if target-key is also a key
3. only thing to note is that there can be duplicated elements, 
    they all need a position in the hash table, hence they should be saved in a list
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hashTable = {}
        for i in range(len(num)):
            if hashTable.has_key(num[i]):
                hashTable[num[i]].append(i+1)
            else:
                hashTable[num[i]] = [i+1]
        for key in hashTable:
            if hashTable.has_key(target-key):
                if key == target-key:
                    return sorted(hashTable[key])[0:2]
                else:
                    return sorted([hashTable[key][0], hashTable[target-key][0]])
            
            
print Solution().twoSum([0,4,3,0], 0)