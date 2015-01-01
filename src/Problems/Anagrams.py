'''
Created on 30 Dec 2014

@author: Yuan
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        map = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in map:
                map[ss] += [s]
            else:
                map[ss] = [s]
        return [s for group in map.values() if len(group) > 1 for s in group]
    
sol = Solution()

print(sol.anagrams(["afda", "dfaa", "adfasfsfa"]))