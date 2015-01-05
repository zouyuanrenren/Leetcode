'''
Created on 4 Jan 2015

@author: Yuan
'''

'''
The basic idea is 3 pointers.
p1 in range(0, len(num)-2)
for each p1:
    p2 in range(p1+1, len(num)-1)
    p3 in range(p2+1, len(mum)) in reverse order
    (optional) if n1 + n2 > 0, break
    if n1 + n2 + n3 > 0, decrease p3 until the next different element
    if n1 + n2 + n3 < 0, increase p2 until the next different element
    if n1 + n2 + n3 == 0, found a resolution, and increase p2 and decrese p3 together
    at the end, increase p1
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3:
            return []
        List = []
        num.sort()
        index1 = 0
        while index1 < len(num) -2:
#             if index1 < len(num)-2:
            if num[index1] > 0:
                break
            index2 = index1+1
            index3 = len(num)-1
            while index2 < index3:
#                 if index2 < index3:
                if num[index1] + num[index2] > 0:
                    break
                SUM = num[index1]+num[index2]+num[index3]
                if SUM > 0:
                    index3 -= 1
                elif SUM < 0:
                    index2 += 1
                else:
                    List.append([num[index1],num[index2],num[index3]])
                    index2 +=1
                    while index2 < index3 and num[index2] == num[index2-1]:
                        index2 += 1
                    index3 -= 1
                    while index2 < index3 and num[index3] == num[index3+1]:
                        index3 -= 1
            index1 += 1
            while index1 < len(num)-2 and num[index1] == num[index1-1]:
                index1 += 1
        return List