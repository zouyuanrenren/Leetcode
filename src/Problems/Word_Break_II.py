'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
This one is similar to word break.
The difference is, instead of maintaining only the sub-strings that can be brobken, also maintain how they can be broken.
We use a dictionary part to maintain such information.
Particularly i in part IFF s[:i] can be broken, and word in part[i] IFF word is the last word in the broken s[:i].

Once part is built, we can start generate the result from part.
It will be easier to do it from the end to the beginning because every word in part[i] leads to a valid break-down in part[i-len(word)].
Particularly, when a word in part[i] is picked, the next word should be chosen from part[i-len(word)]
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
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# s = "leetcode"
# dict = ["leet", "code"]
print len(s)
print sol.wordBreak(s, dict)                        