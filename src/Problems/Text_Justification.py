'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        currentsize = 0
        currentwords = []
        results = []
        for word in words:
            if len(word) > 0:
                if currentsize == 0 or currentsize+len(word)+len(currentwords) <=L:
                    currentsize+=len(word)
                    currentwords.append(word)
                else:
                    if len(currentwords) == 1:
                        results.append(currentwords[0]+" "*(L-currentsize))
                    else:
                        joining = [" " for i in range(len(currentwords)-1)]
                        total = currentsize+len(currentwords)-1
                        start = 0
                        while total < L:
                            joining[start]+=" "
                            start+= 1
                            total +=1
                            if start == len(currentwords)-1:
                                start = 0
                        result = ""
                        for i in range(len(currentwords)-1):
                            result += currentwords[i]+joining[i]
                        result += currentwords[-1]
                        results.append(result)
                    currentwords = [word]
                    currentsize = len(word)
        if len(currentwords) > 0:
            result = " ".join(currentwords)
            result += " "*(L-(currentsize+len(currentwords)-1))
            results.append(result)
        if len(results) == 0:
            results.append(" "*L)
        return results

sol = Solution()
results = sol.fullJustify([""], 0) 
for line in results:
    print line   
                    