'''
Created on 3 Jan 2015

@author: Yuan
'''
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        while len(s)>0 and s[0] in ("+","-"):
            s = s[1:]
        ss = s.split("e")
        if len(ss)>2:
            return False
        base = ss[0]
        if len(base) == 0:
            return False
        sss = base.split(".")
        if len(sss)>2:
            return False
        nums = []
        nums.append(sss[0])
        if len(sss)>1:
            nums.append(sss[1])
            if len(sss[0])+len(sss[1]) == 0:
                return False
        elif len(sss[0]) == 0:
            return False
        if len(ss)>1:
            exp = ss[1]
            while len(exp) > 0 and exp[0] in ("+", "-"):
                exp = exp[1:]
            if len(exp) == 0:
                return False
            nums.append(exp)
        for num in nums:
            for c in num:
                if ord(c)< ord("0") or ord(c) > ord("9"):
                    return False
        return True

print Solution().isNumber("4.")
