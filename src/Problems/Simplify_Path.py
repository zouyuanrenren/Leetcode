'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        current = ""
        path+="/"
        for c in path:
            if c == "/":
                if len(current) > 0:
                    if current == "..":
                        if len(stack) > 0:
                            stack.pop()
                    elif current != ".":
                        current +="/"
                        stack.append(current)
                    current = ""
            else:
                current += c
        result = "/"+"".join(stack)
        if len(result) > 1 and result[-1] == "/":
            return result[:-1]
        return result
    
print Solution().simplifyPath("/home//foo/")                        