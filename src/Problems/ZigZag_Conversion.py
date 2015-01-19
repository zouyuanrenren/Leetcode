'''
Created on 19 Jan 2015

@author: Yuan
'''
'''
Using a list of strings to maintain the strings on each row.
Then move the pointer up and down to put the characters in s to corresponding row.
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        results = []
        for i in range(nRows):
            results.append("")
        if s != "":
            row = 0
            down = True
            for c in s:
                if down:
                    results[row] += c
                    if row + 1< nRows:
                        row += 1
                    elif row - 1 >= 0:
                        row -= 1
                        down = False
                else:
                    results[row] += c
                    if row - 1 >= 0:
                        row -= 1
                    elif row + 1 < nRows:
                        row += 1
                        down = True
        return ""+"".join(results)