'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
The basic idea is 3 pointers. Let us call them p1, p2 and p3 and the numbers they point to n1, n2, and n3, respectively.

First we sort the list in ascending order.
Then for each p1 in range(0, len(num)-2):
    point p1 to the next different element.
    (optional) if n1 * 3 > 0, reak        INVARIANT: n1 + n2 + n3 >= n1 * 3
    for each p2 in range(p1+1, len(num)-1)
        point p2 to the next different element
        (optional) if n1 + n2 * 2 > 0, break    INVARIANT: n1 + n2 + n3 >= n1 + n2 * 2
        for p3 in range(p2+1, len(mum))[::-1]
            point p3 to the next different element
                if n1 + n2 + n3 > 0, decrease p3 until the next different element
                if n1 + n2 + n3 < 0, increase p2 until the next different element
                if n1 + n2 + n3 == 0, found a resolution, and increase p2 and decrease p3 together
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        List = []
        l = len(num)
        
        # sort the list
        num.sort()
        
        for p1 in range(l-2):
            if p1 == 0 or num[p1] != num[p1-1]: # find the next different n1
                
                # optional break
                if num[p1] > 0:
                    break
                
                p2 = p1 +1
                p3 = l-1
                while p2 < p3:  # loop condition

                    # find the next different p2
                    if p2 > p1+1 and num[p2] == num[p2-1]:
                        p2 += 1
                        continue
                    
                    # optional break
                    if num[p1] + num[p2] * 2 > 0:
                        break
                    
                    # find the next different p3
                    if p3 < l-1 and num[p3] == num[p3+1]:
                        p3 -= 1
                        continue
                    
                    # examine the sum
                    SUM = num[p1]+num[p2]+num[p3]
                    if SUM > 0:
                        p3 -= 1
                    elif SUM < 0:
                        p2 += 1
                    else:
                        List.append([num[p1],num[p2],num[p3]])
                        p2 += 1
                        p3 -= 1
        return List

num = [-1, 0, 1, 2, -1, 4]
print Solution().threeSum(num)