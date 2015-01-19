'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
We maintain a list of candidate words for the next line.
    1. If adding the next word does not exceed L, then add it into the list.
    2. Otherwise, add the current list into the result and reinitialise the candidate list with the next word.
        a. when adding a candidate list, separate the following situations.
            i. there is only one word, then append it with trailing spaces.
            ii. there are multiple words, then first separate them with single spaces,
                then increase the separation with extra spaces from left to right until reaching L
    3. at the end, if there is any remaining words in the candidate list, 
        append the results with these words, separated by single spaces.
    4. if there is no results at all, add an empty line of size L.
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
results = sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) 
for line in results:
    print line   
                    