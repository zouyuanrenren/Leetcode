'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
anagrams are words who have another words using exactly the same numbers of same characters.
in other words, two anagrams will have the same sorted string.
Hence the solution to this problem is to build a dictionary that maps sorted strings to original strings
So that anagrams will be maintained with the same key
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        map = {}
        for s in strs:
            ss = "".join(sorted(s))
            map[ss] = [s] if ss not in map else map[ss]+[s]
        return [s for group in map.values() if len(group) > 1 for s in group]
    
sol = Solution()

print(sol.anagrams(["afda", "dfaa", "adfasfsfa"]))