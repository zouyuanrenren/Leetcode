'''
Created on 1 Jan 2015

@author: Yuan
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        return self.peakIn(num, 0, len(num))
    
    def peakIn(self, num, start, end):
        if start >= end:
            return -1
        middle = (end-start)/2+start
        if middle == 0 or num[middle] > num[middle-1]:
            if middle == len(num)-1 or num[middle] > num[middle+1]:
                return middle
            else:
                first = self.peakIn(num, start, middle-1)
                if first > -1:
                    return first
                else:
                    return self.peakIn(num, middle+1, end)
        else:
            if middle == len(num) -1 or num[middle] > num[middle+1]:
                first = self.peakIn(num, start, middle)
                if first > -1:
                    return first
                else:
                    return self.peakIn(num, middle+2, end)
            else:
                first = self.peakIn(num, start, middle)
                if first > -1:
                    return first
                else:
                    return self.peakIn(num, middle+1, end)
                        

print Solution().findPeakElement([1,2,3,4,3])

