'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        part = {0:[]}
        for i in range(1, len(s)+1):
            for word in dict:
                size = len(word)
                if i >= size and s[i-size:i] == word and i-size in part:
                    if i in part:
                        part[i].append(word)
                    else:
                        part[i] = [word]
        results = []
        if len(s) in part:
            self.add(results, [], len(s),part)
        return results
    
    def add(self,results, current, target, part):
        if target == 0:
            results.append(" ".join(current[::-1]))
        else:
            for word in part[target]:
                current.append(word)
                self.add(results, current, target-len(word), part)
                current.pop()
    

sol = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# s = "leetcode"
# dict = ["leet", "code"]
print len(s)
print sol.wordBreak(s, dict)                        