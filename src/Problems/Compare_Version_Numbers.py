'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
One of the easy problems:
1. split the two version numbers by "."
2. append the shorter one with trailing 0s
3. compare each segment

step 2 can be avoided. But in that case after step 3 there might be leftovers from one list.
    depending on which one is left, logics can be different.
'''
class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1)>len(v2):
            for i in range(len(v2), len(v1)):
                v2.append("0")
        elif len(v1) < len(v2):
            for i in range(len(v1), len(v2)):
                v1.append("0")
        for i in range(min(len(v1), len(v2))):
            n1 = int(v1[i])
            n2 = int(v2[i])
            if n1 > n2:
                return 1
            elif n2 > n1:
                return -1
        return 0
    
sol = Solution()
print sol.compareVersion("1.0", "1")