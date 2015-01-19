'''
Created on 3 Jan 2015

@author: Yuan
'''
'''
A typical stack problem.
We need to consider the following cases:
1. if encounter "../", we should pop stack if possible.
2. if encounter "./", we should ignore.
3. if encounter other, we should push stack.
4. we need to remove the last "/" if it is not the only character.
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
    
    def simplifyPath2(self, path):
        stack = []
        list = path.split("/")
        for word in list:
            if word == "..":
                if stack:
                    stack.pop()
            elif word != "." and len(word)>0:
                stack.append(word)
        return "/"+"/".join(stack)
    
print Solution().simplifyPath2("/home//foo/")                        